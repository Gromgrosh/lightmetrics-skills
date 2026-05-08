# Re-review and version comparison

When a re-review is detected (the audit folder's `.state/findings-history.json` exists), the skill produces a versioned diff against the previous run instead of a fresh report.

## State file schema

Path: `Projects/audits/<figma-filename>/<figma-pagename>/.state/findings-history.json`

```json
{
  "page_url": "https://figma.com/design/<fileKey>/...",
  "id_counter": 21,
  "versions": [
    {
      "version": 1,
      "date": "2026-05-08",
      "findings": [
        {
          "id": "F-001",
          "rubric": "wcag",
          "principle": "1.4.3 Contrast (Minimum)",
          "target_node_id": "12:34",
          "issue": "Button label color #9CA3AF...",
          "severity": "Blocker",
          "confidence": "definite"
        }
      ]
    },
    {
      "version": 2,
      "date": "2026-05-12",
      "findings": []
    }
  ],
}
```

## Re-review flow

1. **Detection.** On invocation, after Stage 1 resolves the target file/page, check for `.state/findings-history.json`. If present and parseable, set `mode = re-review`. Otherwise `mode = fresh`.

2. **Run Stages 1-3** as normal, producing fresh "current findings" without IDs assigned yet.

3. **Match current findings against the latest version's findings.** For each current finding `c`:

   **Step a — Primary key match.** Look for a previous finding `p` in the latest version such that:
   - `p.rubric === c.rubric` AND
   - `p.principle === c.principle` AND
   - `p.target_node_id === c.target_node_id`

   If found, this is a match. Continue to step e.

   **Step b — Secondary text match.** If no primary-key match, compute Jaccard similarity between `c.issue` and each previous finding's `issue` (within the same `target_node_id`, ignoring rubric). If any similarity >0.7, treat as match.

   **Step c — Node-renamed fallback.** If still no match, search all previous findings (across rubrics) for one with similarity >0.7 on `issue` regardless of `target_node_id`. If found, treat as match AND flag in the diff: `F-XXX — node may have been renamed/restructured (was at <old_node_id>, now at <new_node_id>); please verify.`

   **Step d — No match.** Treat `c` as a new finding.

   **Step e — Match found.** Inherit the previous finding's ID. If severity differs from previous, record a `severity_change` entry: `{ id, old_severity, new_severity }`.

4. **Identify resolved findings.** Any finding in the latest version with no current match is Resolved. Record its ID.

5. **Assign IDs to new findings.** Use `id_counter` from the state file. Increment after each assignment. Persist updated `id_counter` after the run.

6. **Categorize for the diff section:**
   - `Resolved` — IDs of previous findings with no current match.
   - `Still open` — IDs of findings matched between previous and current. Include severity changes.
   - `New` — IDs assigned to current findings with no previous match.
   - `Renamed/restructured` — IDs flagged in step c.

7. **Update state file.** Append the new version to `versions[]`. Update `id_counter`. Persist to disk.

## Edge cases

- **Page URL changed (file moved/renamed in Figma):** The skill detects this when the `page_url` in the state file no longer matches the input URL but the input matches an existing audit folder via the user's input URL parsing. Behavior: ask the user `"Treat as continuation of the previous audit at <path>, or start a fresh audit folder?"`. Default to start-fresh on the second prompt.
- **Node deleted between runs:** Previous finding's `target_node_id` no longer appears in the current evidence bundle. Treat as Resolved with a note: `F-XXX — node no longer exists; finding marked Resolved.`
- **State file corrupted:** Per pipeline.md, rename to `.state/findings-history.corrupted-<timestamp>.json` and treat run as v1.
- **Two siblings now have the same content** (e.g., a duplicated component): both can match the same previous finding by primary key. Resolve by `target_node_id` exact match first; if still tied, the lower-numbered node ID wins.
