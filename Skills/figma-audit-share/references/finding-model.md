# Finding model

Every rubric module returns findings in this exact schema. The Synthesis stage (Pipeline Stage 3) merges findings across rubrics, so consistency is required.

## Schema

```json
{
  "rubric": "string",
  "principle": "string",
  "target_node_id": "string",
  "target_node_url": "string",
  "issue": "string",
  "evidence": "string",
  "recommended_fix": "string",
  "confidence": "definite | likely | suggestion"
}
```

## Field definitions

- **rubric** — the rubric module name. One of: `nielsen`, `wcag`, `ui-checklist`, `norman`, `ux-writing`.
- **principle** — the specific principle or criterion within the rubric. Examples:
  - Nielsen: `"H4: Consistency and standards"`
  - WCAG: `"1.4.3 Contrast (Minimum)"`
  - UI checklist: `"Visual hierarchy"` / `"Token usage — color"` / `"Typography scale"`
  - Norman: `"Visibility"` / `"Affordances"` / `"Mapping"`
  - UX writing: `"CTA clarity"` / `"Error message helpfulness"` / `"Tone consistency"`
- **target_node_id** — the Figma node ID the finding applies to (with `:` separator, e.g., `"12:34"`).
- **target_node_url** — a Figma deep link to the target node, in the form `figma.com/design/<fileKey>/<fileName>?node-id=<nodeId>`. The orchestrator constructs this from the input URL.
- **issue** — one or two sentences describing what is wrong. Plain language; no jargon. Example: `"Button label color #9CA3AF on background #F3F4F6 — contrast 1.94:1, fails 4.5:1 minimum."`
- **evidence** — one sentence explaining how the rubric concluded this. Examples: `"Computed from variable defs"` / `"Visible in screenshot"` / `"Inferred from token usage in metadata"`. This makes findings traceable.
- **recommended_fix** — one or two sentences with a concrete action. Reference LightSpectrum tokens by name where applicable. Avoid vague suggestions like "improve contrast" — prefer "use --color-on-primary token (#111827) for label."
- **confidence** — one of:
  - `definite` — computed from data (e.g., contrast calculated from variable defs).
  - `likely` — inferred from screenshot or metadata with high probability.
  - `suggestion` — judgment call; reasonable designers could disagree.

## Severity is NOT in the rubric output

Rubric modules do NOT assign severity. Severity is assigned in Stage 3 (Synthesis) per the rules in [severity.md](severity.md). This separation lets rubrics focus on detection without each redefining severity logic.

## Example finding (raw, pre-synthesis)

```json
{
  "rubric": "wcag",
  "principle": "1.4.3 Contrast (Minimum)",
  "target_node_id": "12:34",
  "target_node_url": "https://figma.com/design/abc/Audit?node-id=12:34",
  "issue": "Button label color #9CA3AF on background #F3F4F6 — contrast 1.94:1, fails 4.5:1 minimum.",
  "evidence": "Computed from variable defs (label uses --color-text-disabled, background uses --color-surface-subtle).",
  "recommended_fix": "Use --color-on-primary token (#111827) for label, or darken background to --color-surface-strong.",
  "confidence": "definite"
}
```
