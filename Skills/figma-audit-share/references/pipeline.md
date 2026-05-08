# Pipeline

The figma-audit skill executes 5 stages in strict order on every invocation. Each stage's input is the previous stage's output. Rubric files are loaded **lazily** in Stage 2 — never at startup.

## Stage 1 — Evidence gathering

**Inputs:** one or more Figma URLs from the user.

**Steps:**

1. **Parse each URL** to extract `fileKey` and `nodeId`. URL shapes:
   - `figma.com/design/<fileKey>/<fileName>?node-id=<nodeId>` → standard
   - `figma.com/design/<fileKey>/branch/<branchKey>/<fileName>` → use `branchKey` as `fileKey`
   - `figma.com/board/<fileKey>/<fileName>?node-id=<nodeId>` → FigJam (out of scope for v1; reject with a clear error)
   - `figma.com/slides/<fileKey>/<fileName>?node-id=<nodeId>` → Slides (out of scope for v1; reject)
   - Convert `-` to `:` in `nodeId` parsed from the query string.

2. **Fetch evidence per target node:**
   - `mcp__claude_ai_Figma__get_design_context` (fileKey, nodeId) → returns code + screenshot + design hints
   - `mcp__claude_ai_Figma__get_metadata` (fileKey, nodeId) → returns structural data (children, properties, layout)
   - `mcp__claude_ai_Figma__get_variable_defs` (fileKey, nodeId) → returns LightSpectrum token bindings used in the node and its descendants

3. **Auto-pull sibling frames** when at least one rubric pass needs cross-screen context. Triggers: any rubric whose principles include "consistency", "navigation", "user control across screens".
   - Use `mcp__claude_ai_Figma__get_metadata` on the node's parent to enumerate siblings.
   - "Sibling" = a frame at the same hierarchy level as the target node, on the same Figma page.
   - Cap: up to 4 siblings (configurable). If more than 4 exist, pick the 4 nearest on the canvas (smallest x/y offset from the target).
   - For each sibling, fetch only `get_screenshot` + a lightweight `get_metadata` (no `get_design_context`) — enough for consistency comparison without bloating the evidence bundle.

4. **Cache the evidence bundle in memory** for the rest of the run. Schema:

```typescript
type EvidenceBundle = {
  targets: Array<{
    file_key: string;
    node_id: string;
    node_url: string;
    design_context: object;   // from get_design_context
    metadata: object;          // from get_metadata
    variable_defs: object;     // from get_variable_defs
  }>;
  siblings: Array<{
    file_key: string;
    node_id: string;
    node_url: string;
    screenshot: string;        // base64 or temp path
    metadata_summary: object;
  }>;
};
```

5. **Save screenshots to disk** under `Projects/audits/<file>/<page>/assets/` — one file per target node, named provisionally (e.g., `target-1.png`); they get renamed in Stage 4 once finding IDs are assigned.

**Output:** `EvidenceBundle` cached in memory + screenshots on disk.

## Stage 2 — Rubric evaluation passes

**Inputs:** `EvidenceBundle`.

**Steps:**

For each rubric in this order — `nielsen`, `wcag`, `ui-checklist`, `norman`, `ux-writing`:

1. **Lazy-load** the rubric file: read `references/rubric-<name>.md` (only this file; don't load the others).
2. **Run the rubric pass:** apply each principle in the rubric file to the evidence bundle. For each violation found, emit a finding object per the schema in [finding-model.md](finding-model.md).
3. **Append findings to the run-level raw findings list** (no IDs assigned yet, no severity).
4. **Release the rubric file from active context** before loading the next.

A rubric pass that finds nothing returns an empty list — that's expected and not an error.

**Output:** flat list of raw findings (no IDs, no severity, possibly with duplicates across rubrics).

## Stage 3 — Synthesis

**Inputs:** raw findings list.

**Steps:**

1. **Dedupe.** Two findings collapse into one if they share `target_node_id` AND describe the same underlying issue. Two findings describe the same underlying issue if:
   - Their `principle` fields are equivalent (e.g., WCAG `1.4.3 Contrast` and UI checklist `Token usage — color contrast` on the same hex pair), OR
   - Their `issue` strings are >70% similar (Jaccard similarity over word sets is sufficient).

   The merged finding records all rubrics that flagged it in a `merged_from` array. The most concrete `recommended_fix` wins; the others are dropped.

2. **Assign severity** per [severity.md](severity.md). Read each rubric's `## Severity guidance` section to determine the severity for each principle. When multiple rubrics flagged the same finding, the highest severity wins.

3. **Assign finding IDs.** On a fresh run, IDs start at `F-001`. On a re-review, IDs are assigned per the matching rules in [re-review.md](re-review.md) — still-open findings keep their old ID, new findings get the next ID from the persisted `id_counter`.

4. **Sort findings** by severity (Blocker → Major → Minor → Suggestion), then by ID within severity.

**Output:** synthesized findings list, ready for output generation.

## Stage 4 — Output generation

**Inputs:** synthesized findings list.

**Steps:**

1. **Determine output folder.** From the target node's file and page name (fetched via metadata in Stage 1):
   - `Projects/audits/<figma-filename>/<figma-pagename>/`
   - Sanitize names for filesystem: replace `/`, `\`, `:` with `-`; preserve spaces.

2. **Determine version number.** Check `Projects/audits/<file>/<page>/.state/findings-history.json`:
   - File missing → this is v1.
   - File present → version is `(latest version in file) + 1`.

3. **Rename screenshots** from provisional names to `assets/F-<NNN>.png` matching their finding IDs. If multiple findings target the same node, screenshots are deduplicated (one file per node, referenced by multiple findings).

4. **Write the markdown report** at `Projects/audits/<file>/<page>/audit-v<N>-<YYYY-MM-DD>.md` per the template in [output-templates.md](output-templates.md). Include the diff section if version > 1 (sourced from the re-review delta in Stage 5 — see note below).

5. **Persist state.** Update `Projects/audits/<file>/<page>/.state/findings-history.json` with this run's findings, severity assignments, and the new `id_counter`. See [re-review.md](re-review.md) for the schema.

**Output:** markdown report on disk; state file updated. (No Figma comments are posted — see "Out of scope" in SKILL.md.)

## Stage 5 — Re-review delta

**Triggered only when** `Projects/audits/<file>/<page>/.state/findings-history.json` exists and is readable.

**Inputs:** synthesized findings list (from Stage 3); previous findings list (from `.state/findings-history.json`).

**Steps:**

See [re-review.md](re-review.md) for the matching algorithm and state-file schema. The output of this stage is:

- The diff section (Resolved / Still open / New / Severity changes) for the markdown report (consumed in Stage 4 step 4).
- An updated `.state/findings-history.json` (written in Stage 4 step 5).

**Note on stage ordering:** Stage 5 is conceptually after Stage 3 and before Stage 4 (since Stage 4 needs the diff). In implementation, the orchestrator invokes Stage 5 between Stages 3 and 4 when a re-review is detected.

## Failure modes and recovery

- **Figma URL invalid or unsupported (FigJam, Slides):** Reject in Stage 1 with a clear error message. Do not proceed.
- **Figma MCP returns no data:** Retry once. If still no data, report the failure to the user; do not produce a report.
- **State file corrupted:** Treat as fresh run (v1). Inform the user. Do not overwrite the corrupted file silently — rename it to `.state/findings-history.corrupted-<timestamp>.json` and start fresh.
