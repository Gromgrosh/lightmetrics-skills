# Output template

The skill's single output surface is a **markdown audit report** on disk. Findings have stable IDs (`F-001`, `F-002`, …) assigned during the Synthesis stage; IDs persist across re-review runs (see [re-review.md](re-review.md)).

## Markdown report template

Path: `Projects/audits/<figma-filename>/<figma-pagename>/audit-vN-<YYYY-MM-DD>.md`.

**Finding-block formatting rule:** Each `**Field:**` line in a finding block must be separated from the next by a blank line. Do NOT pack multiple fields into one paragraph — markdown renderers join consecutive lines without a blank line into a single paragraph, which makes the finding hard to scan. Treat the schema below as authoritative for whitespace.

````markdown
# Figma Audit — <Figma file/screen name>

**File:** [<figma-filename>](https://figma.com/design/<fileKey>/...)
**Page:** <figma-pagename>
**Run:** v<N>, <YYYY-MM-DD>
**Rubrics evaluated:** Nielsen 10, WCAG 2.2 AA, UI checklist, Norman, UX writing

## Diff vs. previous run (v<N-1> — <date>)
*(this section is omitted on v1)*

- **Resolved (<count>):** F-04, F-07, F-12
- **Still open (<count>):** F-01, F-02, F-08
  - *Severity changes:* F-02 raised from Major to Blocker
- **New (<count>):** F-19, F-20

## Summary

| Severity | Count |
|---|---|
| 🔴 Blocker | 2 |
| 🟠 Major | 5 |
| 🟡 Minor | 7 |
| ⚪ Suggestion | 4 |

## Findings

### F-001 · 🔴 Blocker · WCAG 1.4.3 (Contrast)

**Where:** "Sign in" button label — [open in Figma](<deep-link>)

**Issue:** Button label color `#9CA3AF` on background `#F3F4F6` — contrast 1.94:1, fails 4.5:1 minimum.

**Evidence:** Computed from variable defs.

**Impact:** Low-vision users cannot read the primary CTA.

**Recommended fix:** Use `--color-on-primary` token (`#111827`) for label, or darken background to `--color-surface-strong`.

**Confidence:** Definite

**Screenshot:** ![](assets/F-001.png)

---

### F-002 · 🟠 Major · UX writing

**Where:** Empty-state copy on Reports list — [open in Figma](<deep-link>)

**Issue:** Copy reads "No data available." Provides no next step or context.

**Evidence:** Visible in screenshot.

**Impact:** Users land on a blank state without knowing why or how to populate it.

**Recommended fix:** "No reports yet. Create your first report or import from CSV." Add a primary action.

**Confidence:** Likely

**Screenshot:** ![](assets/F-002.png)

[... more findings, sorted by severity (Blocker → Major → Minor → Suggestion), then by ID within severity ...]

## Footnotes

*Borderline severity calls noted here for re-review tracking.*

- F-005 — borderline Major / Minor: contrast 4.41:1 (just below threshold). Tracked at Major; re-examine if WCAG 1.4.3 calculation methodology changes.

````

## Severity emoji reference

- 🔴 Blocker
- 🟠 Major
- 🟡 Minor
- ⚪ Suggestion

These appear in the markdown summary table and finding headers.
