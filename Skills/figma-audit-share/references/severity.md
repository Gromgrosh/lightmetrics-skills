# Severity model

Every finding receives one of four severity tiers. This is the canonical definition — every rubric module's `severity guidance` section references back here.

## Tiers

### 🔴 Blocker — must fix before ship

A finding is a Blocker if ANY of these is true:

- **WCAG 2.2 Level AA failure** that is computable from the design:
  - Text contrast below 4.5:1 (or 3:1 for large text — 18pt+ regular or 14pt+ bold)
  - Touch target below 24×24 CSS px (WCAG 2.5.8)
  - Meaningful information conveyed by color alone (WCAG 1.4.1)
- **Primary task is broken or impossible** to complete from the design as drawn (e.g., login screen with no submit affordance; checkout missing payment method).
- **Misleading or wrong copy** that would cause user error or harm (e.g., "Delete" labeled as "Cancel"; pricing in wrong currency; legal copy contradicting policy).
- **Critical interaction state missing** that the user provably needs (e.g., destructive action with no confirmation; required field with no error state).

### 🟠 Major — fix this iteration

A Major if ANY:

- **WCAG AAA failure** where AAA is reasonable for the product context (e.g., 7:1 contrast on text-heavy reports).
- **Clear heuristic violation** likely to confuse most users (Nielsen / Norman). Example: hidden system status during a slow operation; inconsistent navigation between screens.
- **Design-system inconsistency that breaks an established LightSpectrum pattern**:
  - Hardcoded color where a LightSpectrum token exists
  - Component detached from library (a copy of a library component, locally edited)
  - Typography off-scale (a font-size value that does not match a LightSpectrum size token)
- **UX writing**:
  - Unclear CTA (verb is missing or vague — "Submit" instead of "Place order")
  - Jargon that blocks comprehension for non-experts
  - Tone clash between adjacent screens
  - Error message that states the problem but offers no fix

### 🟡 Minor — fix when convenient

A Minor if:

- **Single-screen polish issue** with limited blast radius (e.g., one-off spacing inconsistency; alignment off by a few pixels; orphaned label).
- **Heuristic borderline call** with low user impact.
- **UX writing wordiness** — copy could be tighter, but is correct and clear (e.g., "Click here to continue to the next step" → "Continue").
- **Consistency drift within one screen** — one-off variation that isn't meaningful.

### ⚪ Suggestion — preference, low confidence

A Suggestion if:

- **Aesthetic preference** that reasonable designers could disagree on (e.g., "the icon could be 1px smaller"; "border-radius could be slightly larger").
- **Low-confidence finding** flagged with `confidence: "suggestion"` in the rubric output.
- **Stylistic suggestion** outside the rubric's hard rules.

## Severity assignment rules

1. **Highest wins on merge.** When the Synthesis stage merges findings across rubrics on the same node and same underlying issue, the merged finding takes the highest severity any rubric assigned.
2. **Floor on confidence.** A finding with `confidence: "suggestion"` may not exceed Suggestion severity, regardless of which rubric flagged it.
3. **Borderline calls go lower.** If a finding straddles two tiers, pick the lower one and add a footnote in the markdown report's Footnotes section so re-reviews can re-examine it.
4. **Severity is fixed per run.** A finding's severity does not change mid-run. Severity changes between runs are flagged in the diff section (e.g., `F-002 — severity raised from Major to Blocker`).

## How rubrics map to severity

Each rubric file's `## Severity guidance` section lists which of its principles map to which severity tier. The orchestrator reads severity guidance per rubric, not from this file directly.
