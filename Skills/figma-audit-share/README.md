# figma-audit

A Claude Code skill that audits Figma designs across usability, accessibility, UI, and UX-writing rubrics — producing a versioned markdown report.

## What it evaluates

- **Nielsen 10 usability heuristics** — visibility of system status, match with real world, user control, consistency, error prevention, recognition over recall, flexibility, aesthetic minimalism, error recovery, help & documentation
- **WCAG 2.2 Level AA** (criteria checkable from a static design) — contrast, target size, color use, focus visibility, error identification
- **UI checklist** — visual hierarchy, typography scale, spacing rhythm, token vs. hardcoded color, component consistency
- **Don Norman's design principles** — visibility, feedback, affordances, signifiers, mapping, constraints, conceptual model
- **UX writing** — clarity, CTA verbs, error helpfulness, empty-state guidance, tone, length, correctness

## Output

A markdown report at `Projects/audits/<figma-filename>/<figma-pagename>/audit-vN-<YYYY-MM-DD>.md` — full structured findings with deep-links to each flagged Figma node and screenshots. The skill does not post comments back to the Figma file; the markdown report's deep-links are the navigation surface.

## Re-review

Pass the same Figma URL again after fixing issues. The skill detects the previous audit and produces a diff:

- **Resolved** — findings that no longer reproduce
- **Still open** — findings that persist (with severity-change notes)
- **New** — findings introduced since the last run

Stable finding IDs are preserved across runs.

## Requirements

- **Claude Code** — desktop app, CLI, or VS Code extension
- **Figma MCP** — the official Figma MCP server (`https://mcp.figma.com/mcp`), authenticated for read access to the files you want to audit

That's it. No personal access tokens, no external services.

## Install

From the directory where you've placed this folder, run:

```bash
./install.sh
```

The script symlinks this folder into `~/.claude/skills/figma-audit` and verifies the install. Alternative manual install:

```bash
ln -s "$(pwd)" ~/.claude/skills/figma-audit
```

After install, restart Claude Code (or reload skills) so it picks up the new skill.

## Usage

In Claude Code, invoke the skill conversationally with one or more Figma URLs:

```
"Audit this Figma file: https://figma.com/design/abc/Audit?node-id=12-34"
"Review these screens: <url1> <url2>"
"Re-evaluate the audit at <url>"
```

The skill detects re-reviews automatically (no flag required).

## Folder layout

This bundle:

```
figma-audit-share/
├── SKILL.md                  ← orchestrator (entry point)
├── README.md                 ← this file
├── LICENSE
├── install.sh                ← one-command symlink install
└── references/
    ├── pipeline.md           ← 5-stage execution pipeline
    ├── severity.md           ← Blocker / Major / Minor / Suggestion
    ├── finding-model.md      ← finding schema (rubric ↔ synthesis contract)
    ├── output-templates.md   ← markdown report template
    ├── re-review.md          ← match algorithm + state file format
    ├── rubric-nielsen.md     ← Nielsen 10 heuristics
    ├── rubric-wcag.md        ← WCAG 2.2 AA criteria
    ├── rubric-ui-checklist.md
    ├── rubric-norman.md
    └── rubric-ux-writing.md
```

Per-audit (created on first run, in your workspace):

```
Projects/audits/<figma-filename>/<figma-pagename>/
├── audit-v1-2026-05-08.md
├── audit-v2-2026-05-12.md
├── assets/
│   └── *.png
└── .state/
    └── findings-history.json
```

## Customising for your design system

The `references/rubric-ui-checklist.md` file is tuned to **LightSpectrum**, Lightmetrics' design system. The principles (visual hierarchy, typography scale, spacing rhythm, color tokens, component consistency, alignment, density) are universal, but the specific token names and heuristics reference LightSpectrum.

To adapt for a different design system:

1. Open `references/rubric-ui-checklist.md`
2. Replace LightSpectrum-specific token references with your system's equivalents
3. Adjust the "Severity guidance" thresholds if your team has different definitions of "Major" vs. "Minor"

The other four rubrics (Nielsen, WCAG, Norman, UX writing) are design-system-agnostic and need no adaptation.

## Troubleshooting

- **Re-review treats run as fresh** — The state file at `Projects/audits/<file>/<page>/.state/findings-history.json` is missing or corrupted. Check for `.state/findings-history.corrupted-*.json` (renamed by the skill on a corrupt-state recovery); inspect it manually if needed.
- **Figma URL is FigJam or Slides** — Out of scope for v1. Skill rejects in Stage 1 with an error.
- **Skill not appearing in Claude Code** — Confirm the symlink resolves: `ls -la ~/.claude/skills/figma-audit`. Reload Claude Code to pick up new skills.

## License

MIT. See [LICENSE](LICENSE).

## Source and acknowledgements

Built by Mohit Mitra at Lightmetrics. The five rubrics draw on:

- Jakob Nielsen, *10 Usability Heuristics for User Interface Design* (Nielsen Norman Group, 1994; updated 2024)
- W3C, *WCAG 2.2 Quick Reference*
- Don Norman, *The Design of Everyday Things* (revised 2013)
- Lightmetrics design system conventions for the UI checklist
- General UX-writing principles synthesised from Nielsen Norman, MailChimp Voice & Tone, and Microsoft's Style Guide
