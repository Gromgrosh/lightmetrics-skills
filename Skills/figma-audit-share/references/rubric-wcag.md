# Rubric — WCAG 2.2 Level AA (design-checkable subset)

Source: W3C WCAG 2.2 Quick Reference (https://www.w3.org/WAI/WCAG22/quickref/).

## Overview

This rubric covers WCAG 2.2 success criteria that are checkable from a static Figma design — specifically criteria evaluable from `get_design_context`, `get_metadata`, `get_variable_defs`, and screenshots. AAA criteria are included where the violation is visually detectable; they are flagged as Major per the AAA rule in [severity.md](severity.md).

Out of scope: criteria requiring runtime behavior (keyboard navigation, focus order, screen reader output, animated content, timing). Apply each criterion to the target node and emit findings per the schema in [finding-model.md](finding-model.md). Where a criterion is partially checkable (e.g., focus states only visible when a focus variant is present in the design), note the limitation in the `evidence` field.

## 1.4.1 Use of Color

**Principle:** Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element.

### What to look for in a Figma frame
- Error, warning, and success states: check via screenshot and `get_metadata` whether the state is signaled by color alone (red border, red label) or also by a secondary encoding such as an icon, pattern, or explicit label ("Error", "Required").
- Status indicators (badges, dot indicators, legend items): check whether shape, label, or icon also encodes the meaning.
- Graphs and charts: check whether data series are distinguishable by line style, fill pattern, or data label in addition to hue — visible in screenshot.
- Required field markers: an asterisk (*) alone with a color key in the legend is borderline; it passes if the legend is on the same screen and the asterisk is also explained in text.
- Token usage: `get_variable_defs` may reveal a fill token that maps only to a semantic color role (e.g., `--color-status-error`) with no accompanying icon-presence variable — treat as a signal worth cross-checking in the screenshot.

### Common violations
- Form field error state shown with a red border and red label text only — no error icon, no "Error" text prefix, no inline error message.
- Status badge on a table row uses only a green/amber/red fill with no label text or icon — color-blind users cannot distinguish the three states.
- A line chart renders multiple series using only different hues with no difference in line dash pattern or marker shape.
- A legend in a dashboard maps color swatches to category names with no secondary differentiator; the chart itself has no data labels.

### Severity guidance
- **Blocker:** Information conveyed by color alone with no secondary encoding (confirmed from screenshot or metadata) → Blocker per WCAG AA rule in severity.md.
- **Major:** Partial secondary encoding present (e.g., an icon exists but is visually subordinate and could be missed) → Major, confidence: likely.
- **Minor:** Color is the primary encoding but a non-color differentiator exists (e.g., a dash pattern on a chart) though the association is not obvious → Minor.

## 1.4.3 Contrast (Minimum)

**Principle:** Text and images of text have a contrast ratio of at least 4.5:1 against their background, or 3:1 for large text (18pt+ regular or 14pt+ bold).

### What to look for in a Figma frame
- For every text layer: identify the text fill color and the effective background fill (immediate parent frame or group with a solid fill, or the page background).
- Computed via `get_variable_defs`: if both fills resolve to LightSpectrum tokens with known hex values, calculate the contrast ratio using the WCAG relative luminance formula. Confidence = `definite`.
- If fills are hardcoded hex values visible in `get_metadata`, compute directly. Confidence = `definite`.
- If fills cannot be resolved (e.g., an image background), use the screenshot and flag as confidence `likely` or `suggestion`.
- Large text threshold: 18pt (24px) or larger at regular weight, or 14pt (18.67px) or larger at bold weight. Check font-size and font-weight in `get_metadata`.
- LightSpectrum note: text should use fluid type tokens (e.g., `--font-size-h1`). If `get_variable_defs` shows a fixed-px font size instead of a fluid token, flag that separately under criterion 1.4.4.
- Placeholder text, disabled text: WCAG 1.4.3 formally exempts disabled UI components and decorative text. Note when text appears disabled (via opacity or a disabled-state token) so the finding is not raised as a hard failure.

### Common violations
- Secondary label text using `--color-text-subtle` or `--color-text-disabled` token on a white background where the resolved value fails 4.5:1 — a common mis-application of a low-contrast token to active (not disabled) copy.
- Caption text at 11px–12px in a medium-gray tone on a light-gray card background — both the size and color fall below threshold.
- White label text on a medium-blue button where the specific blue token resolves to a mid-luminance value (e.g., ~3.8:1 — near-miss that passes visually but fails numerically).
- Small badge text (10px semibold) using an amber background token; amber's luminance is high, making dark text required rather than white.

### Severity guidance
- **Blocker:** Text contrast ratio computed below the applicable threshold (4.5:1 normal, 3:1 large) → Blocker per WCAG AA rule in severity.md. Confidence must be `definite` or `likely`; do not raise as Blocker on `suggestion`.
- **Minor:** Contrast ratio is within 0.3 of the threshold and relies on approximate background inference → Minor, with note that re-check is needed when the background is confirmed.

## 1.4.4 Resize Text

**Principle:** Text can be resized up to 200% without loss of content or functionality, except for captions and images of text.

### What to look for in a Figma frame
- Check font sizes in `get_metadata` for all text layers. Fixed pixel values (e.g., `fontSize: 14`) that do not correspond to a LightSpectrum fluid type token indicate sizes hardcoded outside the token system.
- LightSpectrum fluid type tokens (`--font-size-h1`, `--font-size-body`, etc.) scale with viewport via `clamp()` — these comply. Fixed `-min` and `-max` token variants are intended for print, email, and JS sizing only — flag if used on a web screen.
- In Figma, evaluate: is text in a fixed-height container with `overflow: hidden` semantics (i.e., the frame has a fixed height and `clip content` is enabled)? If so, text growth at 200% may be clipped — visible when the text layer height is set to a fixed value equal to the current font size * line height with no breathing room.
- Images of text (rasterized type, text embedded in a PNG export) cannot resize — flag these.

### Common violations
- Body text at a hardcoded `fontSize: 12` in `get_metadata`, not bound to a LightSpectrum token — will not participate in the fluid type scale and may not scale in a user's browser accessibility settings.
- A status label placed inside a fixed-height chip frame where the frame height equals `line-height * 1` — any text enlargement will clip the label.
- A dashboard tile renders its KPI number as a PNG export with text baked in — cannot be resized by the browser.
- Using the `-min` variant of a fluid token (e.g., `--font-size-body-min`) on a responsive web component instead of the fluid token (`--font-size-body`) — freezes text at the minimum size.

### Severity guidance
- **Blocker:** Text rendered as an image (rasterized) on a primary interaction surface — the user cannot resize it at all → Blocker.
- **Major:** Hardcoded fixed-px font size not bound to a LightSpectrum token, or incorrect use of `-min`/`-max` variant on a web screen → Major (design-system inconsistency rule in severity.md applies; also an accessibility risk).
- **Minor:** Fixed-size text in a purely decorative or non-interactive context (e.g., a watermark, a legally-required footnote that must remain at a specific size for print parity) → Minor with note.

## 1.4.11 Non-text Contrast

**Principle:** The visual presentation of UI components and meaningful graphical objects has a contrast ratio of at least 3:1 against adjacent colors.

### What to look for in a Figma frame
- Form input borders: compare the border fill to the background behind the input. `get_variable_defs` will resolve both fills if tokens are used. Minimum 3:1 required.
- Button borders on non-solid backgrounds (outlined/ghost buttons): compare button stroke fill to its container background.
- Focus indicator rings (if present as a visible layer in the design): compare focus ring fill to the surface behind it.
- Meaningful icons (those that carry information, not purely decorative): compare icon fill to its immediate background.
- Checkboxes, radio buttons, toggle thumbs: compare the component's distinguishing fill/stroke to the page or form background.
- Graphs: compare meaningful graphical marks (bars, line segments, data points) to the plot background.
- LightSpectrum tokens: `get_variable_defs` may reveal that an input border uses `--color-border-subtle` — check if that token's resolved value achieves 3:1 against `--color-surface-default`.

### Common violations
- Ghost button with a stroke using `--color-border-subtle` (#D1D5DB on white) — contrast approximately 1.6:1, well below 3:1.
- Text input with a light-gray border (#E5E7EB) on a white form background — contrast approximately 1.3:1; the field boundary is nearly invisible.
- Checkbox unchecked state uses only a 1px border in `--color-border-subtle` on a white card — the component is present but its boundary fails 3:1.
- A line chart's gridlines are drawn in the same token as the data line at the same weight — the data line does not achieve 3:1 against the gridlines or background.
- A toggle switch in the off state uses a light-gray thumb on a white background — 3:1 not achieved, users cannot determine interactive state from shape alone.

### Severity guidance
- **Blocker:** UI component boundary (button border, input border, checkbox border) fails 3:1 contrast against its background — computed from variable defs with confidence `definite` → Blocker per WCAG AA rule in severity.md.
- **Major:** Meaningful icon or graphical object below 3:1 where the iconography carries required information → Major.
- **Minor:** Decorative separator or non-essential graphical object below 3:1 (the object does not carry required information) → Minor.

## 2.4.7 Focus Visible

**Principle:** Any keyboard-operable user interface has a mode of operation where the keyboard focus indicator is visible.

### What to look for in a Figma frame
- Focus state design is only checkable if the design includes a dedicated focus variant, hover/focus component variant in the Figma component set, or an annotated "focus" state frame.
- Check `get_metadata` for component variant properties: look for `State=Focus`, `State=Focused`, or equivalent property names. If the component set defines no focus variant, the focus state has not been designed.
- Check whether interactive elements (buttons, links, inputs, selects, toggles, checkboxes, radios, tab panels) each have a corresponding focus variant or focus annotation in the file.
- If a focus ring is present, check it against 1.4.11: the ring should achieve 3:1 contrast against both the adjacent element color and the page background. Check via `get_variable_defs`.
- WCAG 2.4.11 (Focus Appearance, AA since 2.2) additionally requires the focus indicator to be at least 2px wide and enclose the perimeter — check ring stroke width in `get_metadata` if visible.

### Common violations
- A primary button component in the Figma library has Default, Hover, Disabled, and Loading variants — but no Focus or Focus-Visible variant. The focus state was never designed.
- A custom tab-panel navigation component has no focus ring annotation; all interactive tabs render identically in every variant shown in the design.
- A focus ring is present but uses `--color-focus-ring` at 1px width on a white background, resolving to #60A5FA — contrast ratio against white is 2.8:1, failing 3:1 under 1.4.11.

### Severity guidance
- **Note on detectability:** If the design contains no focus variant at all and includes interactive elements, emit a finding. Severity = Major (AA criterion; failure to design a focus state is a clear heuristic gap, but the runtime implementation could still comply — hence Major rather than Blocker).
- **Major:** Interactive element(s) present with no focus variant defined anywhere in the component set or frame annotations → Major, confidence: `likely`.
- **Blocker:** A focus ring is present and explicitly shown, but the ring's contrast ratio against the adjacent color fails 3:1 (computed) → Blocker per 1.4.11 (Non-text Contrast).
- **Minor:** Focus variant exists but is applied inconsistently (some components have it, some do not) → Minor.

## 2.5.5 Target Size (Enhanced)

**Principle:** The size of the target for pointer inputs is at least 44×44 CSS pixels. (WCAG 2.5.5 is AAA.)

**Note:** This is a WCAG AAA criterion. Per [severity.md](severity.md), AAA failures are Major when AAA is reasonable for the product context.

### What to look for in a Figma frame
- Measure the bounding box (width × height) of interactive elements in `get_metadata` (`absoluteBoundingBox` or `size`). Target includes any padding area designed as part of the tap/click zone.
- Candidates to check: icon buttons, close buttons (×), inline text links, small toggles, tooltip triggers, pagination arrows, chip remove buttons, table row action icons.
- Figma frames are typically designed at 1× or 2×; confirm the scale from the design file's frame width relative to a known device width before comparing to 44px.
- Padding-only targets: if a 16×16 icon has 14px padding on each side, the effective target is 44×44 — this passes. Check if padding is included in the frame or is only CSS-applied.

### Common violations
- Icon-only close button on a modal designed at 20×20 with no padding frame — effective target is 20×20, failing 44×44.
- "Remove" chip button (×) at 16×16 with 4px padding = 24×24 effective — fails 44×44.
- Inline text links inside a dense table at 14px line-height — click target is the text bounding box only, well below 44px height.
- Pagination "Previous / Next" arrow icons at 32×32 with no additional hit area — fails 44×44.

### Severity guidance
- **Major:** Interactive element below 44×44 effective target size — AAA failure where AAA is a reasonable standard for a B2B product used on desktop and touch devices → Major per the AAA rule in severity.md.
- **Minor:** Target is between 40×40 and 44×44 (near-miss) → Minor with note.
- **Suggestion:** Element is primary-desktop-only and touch access is extremely unlikely → Suggestion, confidence: `suggestion`.

## 2.5.8 Target Size (Minimum)

**Principle:** The size of the target for pointer inputs is at least 24×24 CSS pixels, or the target is offset from all adjacent targets by at least 24px spacing. (WCAG 2.5.8 is AA.)

### What to look for in a Figma frame
- Measure bounding box of interactive elements in `get_metadata` as with 2.5.5 above.
- The 24×24 minimum applies unless an offset exception applies: if a target is smaller than 24×24 but there is at least 24px of space between its bounding box and the bounding box of any adjacent interactive element, it passes the offset exception.
- Check spacing between interactive elements (e.g., toolbar buttons, inline action icons) using the `absoluteBoundingBox` of adjacent nodes.
- For inline text links: the target height equals the computed line-height in CSS. At typical body sizes (14–16px), line height may only be 20–24px — check the frame's text style in `get_metadata`.

### Common violations
- A toolbar with six icon buttons packed at 20×20 with 4px gaps — both the target size (20px) and the offset (4px) fail 2.5.8.
- A table's row-level action icons (edit, delete, view) at 16×16 with 8px spacing between them — target size 16px fails, offset 8px also fails.
- A checkbox at 16×16 with no padding — target size fails; only passes if adjacent interactive elements are 24px away.
- A date picker's day cells at 22×22 with 2px gaps — below 24×24 and offset is insufficient.

### Severity guidance
- **Blocker:** Interactive element below 24×24 with no offset exception — computed from `absoluteBoundingBox` values in `get_metadata` → Blocker per WCAG AA rule in severity.md, confidence: `definite`.
- **Major:** Target is exactly 24×24 but offset exception is not met (adjacent target is within 24px) → Major, as the compound condition fails.
- **Minor:** Target meets 24×24 but is below 44×44 (see 2.5.5) — note the shortfall against the enhanced threshold separately.

## 3.3.1 Error Identification

**Principle:** If an input error is automatically detected, the item that is in error is identified and the error is described to the user in text.

### What to look for in a Figma frame
- For every form in the design: check whether an error state variant exists for each input field (`get_metadata` component variants or separate error-state frames).
- The error state must include a text description — an icon alone does not satisfy this criterion. Check for an inline error message text layer below or adjacent to the field.
- The error message must identify which field is in error (typically it is anchored near the field, making identification implicit) and describe what went wrong in text.
- Use `get_metadata` to enumerate all form inputs; cross-check with the frame's variant structure or sibling frames to confirm an error variant exists.
- Check that required fields are marked (asterisk, "Required" label) as a prerequisite — if fields are not marked required, users cannot anticipate which fields will trigger errors.

### Common violations
- Form design shows only a "happy path" frame — no error state variants exist for any field.
- Email field error state shows only a red border and a warning icon, no text message — violation (icon alone is insufficient).
- A multi-field form shows one generic banner error ("Please correct the errors") with no per-field identification — fails because the item in error is not individually identified.
- Password field error state exists but the message reads "Invalid" without specifying the constraint violated (length, character requirements, etc.).

### Severity guidance
- **Blocker:** Form design with no error state variant for any input → Blocker (critical interaction state missing per severity.md; aligns with H9 Nielsen finding — merge in Synthesis).
- **Major:** Error state exists but consists of color/icon only (no error text) → Major (overlaps with WCAG 1.4.1; merge in Synthesis).
- **Minor:** Error text is present but generic ("Invalid input") rather than descriptive → Minor (overlaps with UX writing rubric; merge in Synthesis).

## 3.3.3 Error Suggestion

**Principle:** If an input error is detected and suggestions for correction are known, the suggestion is provided to the user, unless it would jeopardize the security or purpose of the content.

### What to look for in a Figma frame
- For each error state variant identified under 3.3.1: check whether the error message text offers a concrete fix, not just a description of the problem.
- "Your email is invalid" → describes the problem but offers no fix — violation.
- "Enter a valid email (e.g. name@example.com)" → describes the problem and offers a fix — compliant.
- Check `get_metadata` text content of error message layers. If the error message text contains only a description of what is wrong (no instruction or example), flag it.
- Security exception: password strength errors that do not reveal the full ruleset (for security reasons) are exempt from suggesting the exact fix — note this when the field is a password field.

### Common violations
- An email field error message reads "Invalid email address" with no example or guidance on the expected format.
- A date field error reads "Date is out of range" without indicating the valid range.
- A phone number field error reads "Invalid phone number" without specifying the format expected (e.g., "+1 (555) 000-0000" or "10 digits, no dashes").
- A form-level error banner reads "Submission failed" with no actionable guidance on what the user should do.

### Severity guidance
- **Major:** Error message describes the problem with no fix suggestion → Major. Per severity.md, UX writing that states a problem but offers no fix is Major. This criterion overlaps with Nielsen H9; merge findings in Synthesis to avoid duplicate reporting.
- **Minor:** Error message offers a vague fix ("Please check your entry") rather than a specific one — not a clear failure but a quality gap → Minor.
- **Note:** This is an AA criterion, but the failure is not computationally measurable — it requires reading the error message text and evaluating whether a fix is offered. Confidence is therefore `likely` for text-content assessments; `definite` only when the error message text layer is readable from `get_metadata` or the screenshot.

## Output template

Each finding follows the schema in [finding-model.md](finding-model.md). Set:

- `rubric: "wcag"`
- `principle: "<criterion-id> <criterion-name>"` (e.g., `"1.4.3 Contrast (Minimum)"`)

Severity is assigned in Stage 3 (Synthesis) per [severity.md](severity.md), using the severity guidance in each criterion's section above.
