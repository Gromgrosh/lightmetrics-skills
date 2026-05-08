---
name: figma-audit
description: Use when the user asks to audit, evaluate, review, or critique a Figma design (passes one or more Figma URLs with review intent). Produces a versioned markdown audit report with stable finding IDs. Evaluates against Nielsen 10 heuristics, WCAG 2.2 AA, a LightSpectrum-aware UI checklist, Norman design principles, and UX writing. Re-runs against the same URL produce a diff (Resolved / Still open / New).
---

# figma-audit

A multi-pass evaluator for Figma designs. On every invocation, runs all rubrics — there are no mode flags. Output is a markdown report; comments are not posted to the Figma file.

## When to use

Trigger when the user passes one or more Figma URLs and asks for an audit, evaluation, review, or critique. Examples:
- "Audit this Figma file: <url>"
- "Review this design: <url>"
- "Evaluate this against accessibility: <url>"

If the user only wants ONE specific check (e.g., "is this contrast OK?") and doesn't want a full audit, do not invoke this skill — answer directly.

## Pipeline

This skill executes 5 stages strictly in order. The full contract for each stage is in [references/pipeline.md](references/pipeline.md). High level:

1. **Evidence gathering** — fetch design context, metadata, variable defs (and sibling frames if needed) from Figma MCP. Cache once per run.
2. **Rubric evaluation passes** — load each rubric file lazily, run its principles against the evidence, return raw findings. Rubrics: nielsen, wcag, ui-checklist, norman, ux-writing.
3. **Synthesis** — dedupe overlapping findings, assign severity per [references/severity.md](references/severity.md), assign stable finding IDs.
4. **Output generation** — write the markdown report under `Projects/audits/<file>/<page>/`. Screenshots saved to `assets/`. State persisted to `.state/findings-history.json`.
5. **Re-review delta** — only when a previous audit exists for this page. See [references/re-review.md](references/re-review.md).

**Lazy loading is mandatory.** Never read all rubric files at startup. Read each rubric only when running its pass; release before loading the next.

## How to invoke

Always work through these prerequisites:

1. **URL parsing.** Per [references/pipeline.md](references/pipeline.md). Reject FigJam (`figma.com/board/...`) and Slides (`figma.com/slides/...`) URLs in Stage 1 with a clear error.

2. **Evidence reads use Figma MCP tools directly:** `get_design_context`, `get_metadata`, `get_screenshot`, `get_variable_defs`. These do not require JS execution. No `figma:figma-use` prerequisite is needed.

## Outputs

- **Markdown report** at `Projects/audits/<figma-filename>/<figma-pagename>/audit-vN-<YYYY-MM-DD>.md` — full structured findings, deep-links to nodes, screenshots in `assets/`. Format in [references/output-templates.md](references/output-templates.md).
- **State file** at `Projects/audits/<file>/<page>/.state/findings-history.json` — tracks every finding across versions. Used by re-review for diff matching and stable ID continuity.

The skill does NOT post comments to the Figma file. The markdown report's deep-links are the navigation surface.

## Reference files

- [references/pipeline.md](references/pipeline.md) — full pipeline contract
- [references/severity.md](references/severity.md) — Blocker / Major / Minor / Suggestion definitions
- [references/finding-model.md](references/finding-model.md) — finding schema
- [references/output-templates.md](references/output-templates.md) — markdown report template
- [references/re-review.md](references/re-review.md) — match algorithm and state file
- [references/rubric-nielsen.md](references/rubric-nielsen.md)
- [references/rubric-wcag.md](references/rubric-wcag.md)
- [references/rubric-ui-checklist.md](references/rubric-ui-checklist.md)
- [references/rubric-norman.md](references/rubric-norman.md)
- [references/rubric-ux-writing.md](references/rubric-ux-writing.md)

## Out of scope

- Mode flags. Always run all rubrics.
- Posting comments back to Figma. Markdown report only.
- Notion / HTML output. Markdown only.
- FigJam and Slides files.
- Multi-language UX-writing checks beyond English.
- Code-side fix suggestions when the design is implemented (see `impeccable` for live-UI review).
