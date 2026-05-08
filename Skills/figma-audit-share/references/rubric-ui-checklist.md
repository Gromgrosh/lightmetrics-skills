# Rubric — UI checklist (LightSpectrum-aware)

Source: Lightmetrics design system conventions; LightSpectrum token library.

## Overview

This rubric covers UI craftsmanship checks specific to Lightmetrics designs, with heavy emphasis on LightSpectrum design system conformance. The Lightmetrics product is mid-migration from Angular to React — LightSpectrum tokens are being built incrementally: color is in Phase 2 (in-progress, tracked in a Google Sheet); typography, spacing, radius, and motion use the pre-Phase-2 token files (`lightspectrum.tokens.json` + `lightspectrum.css`) as the live reference. A core concern across every principle is token compliance: hardcoded colors, font sizes, and spacing values create maintenance debt and silently break theme switching (`data-theme` attribute: `light`, `dark`, `secondary`, `secondary-dark`). The key detection mechanism is `get_variable_defs` — a Figma MCP call that returns variable bindings on a node; the absence of a binding on a fill, stroke, or text property indicates a hardcoded value.

Apply each principle to the target node and its visible sibling context where available. Emit a finding per principle violation, following the schema in [finding-model.md](finding-model.md). Severity is assigned in Stage 3 (Synthesis) per [severity.md](severity.md).

## Visual hierarchy

**Principle:** The primary action on any screen or card must read as visually primary — heavier weight, stronger fill, or more prominent position than all secondary and tertiary actions. Multiple CTAs at the same visual weight compete for attention and leave users uncertain what to do next.

### What to look for in a Figma frame

- Identify all interactive elements (buttons, links, icon buttons) visible in the frame. Check their fill, stroke, size, and typographic weight via `get_metadata`, which returns each layer's `fills`, `strokes`, and `style` properties.
- If two or more buttons share the same fill color, font weight, and size with no other visual differentiator, they are visually equivalent and compete as co-primaries — flag this.
- Check `get_variable_defs` for fill variable bindings: a primary button should bind to a high-prominence token such as `--color-action-primary` (or equivalent). If two buttons both bind to the same high-prominence token, that is a duplicate primary CTA.
- Use the screenshot (via `get_screenshot`) to cross-check: a true visual hierarchy issue will be immediately visible — two buttons of similar color, weight, and scale sitting side-by-side.
- Check whether secondary actions are styled with an outline or ghost variant, or a lower-hierarchy text link. If `get_metadata` shows matching `fills` between a primary and a secondary action, flag as a hierarchy gap.
- Verify that the most important action is spatially prominent (placed first in reading order, not pushed below a fold or visually de-emphasized by surrounding content).

### Common violations

- A form footer shows two solid-filled, equal-weight buttons ("Save" and "Cancel") using the same button size and fill token — no visual distinction between the primary and dismissal action.
- A dashboard card renders "Edit", "Duplicate", and "Delete" as three identically-styled filled buttons. Destructive and non-destructive actions have equal visual weight; no primary action is apparent.
- A modal's CTA and its close action both use `--color-action-primary` fill — `get_variable_defs` confirms both share the same token, making them visually indistinguishable to scanning eyes.

### Severity guidance

- **Major:** Two or more CTAs share the same visual weight and fill token with no other differentiator, making the primary action unclear → Major (design-system inconsistency rule; overlaps with Nielsen H8 — merge findings in Synthesis).
- **Minor:** Primary CTA is visually dominant but a secondary action could be further de-emphasized (e.g., filled outline where a text link would suffice) → Minor.
- **Suggestion:** Spatial placement of the primary CTA is non-standard (e.g., left-aligned where right-aligned is conventional) but visual weight still reads correctly → Suggestion.

## Typography scale

**Principle:** All text on web screens must use LightSpectrum fluid type tokens (e.g., `--font-size-h1`, `--font-size-text-main`). Hardcoded pixel font sizes bypass the fluid type scale, preventing responsive resizing and breaking cross-theme consistency. The fixed `-min` and `-max` token variants (e.g., `--font-size-h1-min`, `--font-size-body-max`) are reserved for print, email, and JS sizing only.

### What to look for in a Figma frame

- Call `get_metadata` on text layers: it returns `fontSize`, `fontWeight`, `fontFamily`, and `textStyleId`. A named text style (`textStyleId` present) means the layer uses a shared Figma text style, which should correspond to a LightSpectrum token. A missing `textStyleId` means the font size was set locally as a raw pixel value — flag this.
- Call `get_variable_defs` on the same text layers: it returns any variable bindings on the node's properties. A font-size variable binding to a LightSpectrum fluid token (e.g., `--font-size-h1`) confirms compliance. Absence of a binding while `fontSize` is a fixed pixel value confirms a hardcoded override.
- Check for misuse of `-min` or `-max` token variants on web screen contexts. If `get_variable_defs` returns a binding to `--font-size-h1-min` or `--font-size-body-max` on a responsive web frame, flag it — these variants are reserved for print and email.
- `--font-size-text-main` is intentionally fixed at 14px and does not scale — this is the known exception. Do not flag 14px body text if it correctly binds to `--font-size-text-main`.
- Check `fontFamily` in `get_metadata`: all web text should use the LightSpectrum-specified typeface. A different font family on a local text layer indicates an out-of-system override.

### Common violations

- A section heading has `fontSize: 24` in `get_metadata` with no `textStyleId` and no variable binding in `get_variable_defs` — hardcoded pixel value, not using a fluid token.
- A card label uses `--font-size-body-min` as its bound token — `get_variable_defs` shows the `-min` variant. On a web screen, this freezes the text at the minimum size and does not scale, violating the fluid typography rule.
- A custom annotation text layer overrides the font family with a non-LightSpectrum typeface. `get_metadata` shows `fontFamily: "Inter"` where the design system typeface is specified as something else.
- A modal title is manually set to `fontSize: 20` with `fontWeight: 700`, matching the visual appearance of `--font-size-h3` but not bound to it — creating a silent drift that will break when the token value changes.

### Severity guidance

- **Major:** Text layer with a hardcoded `fontSize` not bound to any LightSpectrum token → Major (design-system inconsistency rule in severity.md).
- **Major:** Text layer bound to a `-min` or `-max` token variant on a web screen context → Major (violates the fluid typography rule; also an accessibility risk per WCAG 1.4.4 — merge with WCAG finding in Synthesis).
- **Minor:** Text uses a shared Figma text style but the style name does not correspond to a known LightSpectrum token name (naming drift, not a value drift) → Minor.
- **Suggestion:** Font weight or letter-spacing locally overridden while the font-size token is correctly bound → Suggestion (style drift without token divergence).

## Spacing rhythm

**Principle:** All spacing values — padding, margin, gap, and positional offsets — must reference LightSpectrum spacing tokens. Arbitrary pixel values for spacing create visual inconsistency, accumulate as maintenance debt, and break the systematic rhythm that makes the product feel cohesive across screens.

### What to look for in a Figma frame

- Call `get_variable_defs` on the target frame and its child layers: it returns variable bindings for all bound properties, including `paddingTop`, `paddingBottom`, `paddingLeft`, `paddingRight`, `itemSpacing` (gap), and positional offsets. A bound spacing value points to a LightSpectrum spacing token. The absence of a binding on any spacing property while a non-zero value is present in `get_metadata` indicates a hardcoded spacing value.
- Check `get_metadata` for auto-layout properties: `paddingTop`, `paddingBottom`, `paddingLeft`, `paddingRight`, `itemSpacing`. Each should be zero (intentional no-gap) or bound to a token. Unbound non-zero values are hardcoded spacing — flag these.
- For non-auto-layout frames, check `absoluteBoundingBox` offsets of child nodes against their parent. Irregular offsets (values not corresponding to known token sizes: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64) suggest hardcoded positioning.
- Verify consistent internal rhythm: compare padding and gap values across sibling components. If similar components (e.g., form fields) use differing spacing values (`itemSpacing: 12` on one, `itemSpacing: 14` on another) check whether both are token-bound or whether one is a drift.

### Common violations

- A card component has `paddingTop: 20`, `paddingRight: 20`, `paddingBottom: 20`, `paddingLeft: 20` in `get_metadata` with no variable binding in `get_variable_defs` — 20px is not a LightSpectrum spacing token value; the padding was set by hand.
- A form layout uses `itemSpacing: 14` between fields. The nearest LightSpectrum spacing tokens are 12px and 16px; `get_variable_defs` shows no binding, confirming this is an arbitrary intermediate value.
- Two versions of the same list component use different gap values (`itemSpacing: 8` vs. `itemSpacing: 10`) — one is token-bound, the other is a drift copy. `get_variable_defs` returns a binding on one and nothing on the other.
- A banner element is positioned 6px from the viewport edge. The closest token is 8px; the 6px value is not token-bound, indicating a pixel-pushed placement.

### Severity guidance

- **Major:** Auto-layout spacing property (padding or gap) with a non-zero hardcoded value not bound to a LightSpectrum spacing token → Major (design-system inconsistency rule in severity.md).
- **Minor:** Spacing value is a token-bound but applied inconsistently across siblings on the same screen (token-bound drift, not a raw pixel drift) → Minor.
- **Minor:** Non-auto-layout positional offset that is off by 1–2px from the nearest token value (pixel-push rather than systematic override) → Minor.
- **Suggestion:** Spacing value matches a valid token amount but uses a token intended for a different semantic role (e.g., using a component-internal gap token for page-level spacing) → Suggestion.

## Color usage — tokens vs. hardcoded

**Principle:** Every color fill and stroke in the design must be bound to a LightSpectrum color token. Hardcoded hex values bypass the token system entirely — they do not respond to theme switching (`data-theme`), do not participate in dark-mode inversion rules, and accumulate invisibly as maintenance debt. LightSpectrum color is in Phase 2 (in progress); any fill where a token already exists for that semantic role must use it.

### What to look for in a Figma frame

- Call `get_variable_defs` on every node with a visible fill or stroke. Variable bindings on `fills[*].color` or `strokes[*].color` pointing to a LightSpectrum color variable confirm token compliance. Absence of a binding while a non-transparent fill is present in `get_metadata` confirms a hardcoded color.
- Check `get_metadata` for `fills` and `strokes` arrays: hardcoded colors appear as `type: "SOLID"` with `color: {r, g, b, a}` values and no corresponding variable binding in `get_variable_defs`. When a LightSpectrum token exists for the semantic role (e.g., `--color-surface-default` for a card background, `--color-action-primary` for a primary button fill), flag the hardcoded value.
- Cross-reference discovered hex values against the LightSpectrum variable set returned by `get_variable_defs` for the file. If the hex value matches a token's resolved value in the current theme, it is a "shadow match" — the screen looks correct now but will break on theme switch. Flag shadow matches as a Major finding.
- Dark-mode inversion rule: `Brand-Variant-dark` tokens use the 50-level value in dark mode (instead of 950). If a fill is hardcoded to a 950-level hex and the frame is a dark-mode screen, it will not invert — confirm via the token mapping and flag.
- Opacity-only fills: a fill set to a solid color at reduced layer opacity is a hardcoded workaround. LightSpectrum provides semantic alpha tokens for this purpose. Flag these when a semantic alpha token exists.

### Common violations

- A card background has `fills: [{type: "SOLID", color: {r: 0.95, g: 0.95, b: 0.97}}]` with no variable binding — a hardcoded near-white that matches `--color-surface-subtle` visually but will not flip in dark mode.
- A primary button fill is hardcoded to `#2563EB` — `get_variable_defs` returns no binding. The LightSpectrum token `--color-action-primary` resolves to the same hex in light mode, making this a silent shadow match. In dark mode or `secondary` theme, the button will remain `#2563EB` instead of responding to the theme.
- A status badge background uses `#FEF3C7` with no variable binding — a hardcoded amber that matches the warning-surface token visually but bypasses it entirely.
- A divider line uses a solid fill at 20% layer opacity instead of binding to an alpha color token, creating an opacity-based workaround that breaks in dark mode.

### Severity guidance

- **Major:** Fill or stroke with a hardcoded hex where a LightSpectrum color token exists for that semantic role (including shadow matches) → Major (design-system inconsistency rule in severity.md).
- **Major:** Opacity-layer workaround where a semantic alpha token exists in LightSpectrum → Major.
- **Minor:** Hardcoded color on a purely decorative element (e.g., a placeholder illustration) where no semantic token covers that exact usage → Minor with note.
- **Suggestion:** Fill uses the correct token family but a different semantic variant than expected (e.g., `--color-surface-strong` where `--color-surface-default` is conventional for this component) → Suggestion.

## Component consistency

**Principle:** All instances of LightSpectrum library components must remain attached to the library source. A detached instance — a frame that was originally a library component but has been ungrouped or "Detach instance"-d — diverges silently from the library as the design system evolves. It will not receive updates and may already differ from the canonical component.

### What to look for in a Figma frame

- Call `get_metadata` on every frame in the target: look for the `componentId` field. A node with a `componentId` is an attached component instance. A node that visually resembles a library component but lacks a `componentId` (or where `componentId` is null/absent) is a detached instance — flag it.
- Cross-reference with `get_design_context`: it returns component hints and Code Connect mappings. If a frame visually matches a known LightSpectrum component (by name pattern, layer structure, or screenshot match) but has no component binding in metadata, flag as likely detached.
- Use `get_screenshot` to visually compare suspected detached instances against their library counterpart. Drift in corner radius, shadow, spacing, or icon choice relative to the library spec is a secondary signal.
- Check for "local component" names (components defined in the current file rather than imported from the library): `get_metadata` will not return a library `key` on local components. A local component that mirrors a library component is effectively a detached fork — flag this.
- Pay special attention to form inputs, buttons, badges, and navigation elements — these are the most frequently detached components in the Lightmetrics product.

### Common violations

- A "Primary Button" frame in the design has no `componentId` in `get_metadata` — it was once an instance but was detached and manually restyled, now drifting from the library. The fill color matches the current library token, masking the divergence.
- A text input field has `componentId: null` — the designer detached it to override the internal icon slot, creating a one-off variant instead of using the library's icon slot property.
- A card component is rebuilt locally from scratch as a frame with auto-layout, visually matching the library card. `get_metadata` shows no `componentId` and no library key — it is a shadow copy that will not receive library updates.
- A navigation sidebar is composed of locally-defined list-item components that visually match the library's `NavItem` component but are separate local frames — any update to `NavItem` in the library will not propagate.

### Severity guidance

- **Major:** A library component (button, input, badge, nav item, card) has been detached — `get_metadata` shows no `componentId` on a node that should be a component instance → Major (design-system inconsistency rule in severity.md).
- **Minor:** A local component variant exists that mirrors a library component but is used only once (isolated one-off rather than a systematic fork) → Minor with recommendation to replace.
- **Suggestion:** A structural wrapper frame (e.g., a layout grid, a section frame) is not a component instance — this is expected and not a violation → do not flag wrappers and layout frames as detached components.

## Alignment and grid

**Principle:** All elements in a frame should align to a consistent spatial grid. Off-by-pixel placements fragment the visual rhythm, create perceptible inconsistency in production (especially on high-density displays), and signal that auto-layout or constraint logic was bypassed.

### What to look for in a Figma frame

- Call `get_metadata` on child nodes: it returns `absoluteBoundingBox` (x, y, width, height) for every node. Check whether x/y positions of sibling elements align to a consistent grid increment (4px, 8px, or the LightSpectrum grid baseline). Values such as x=13, y=7, or x=33 where adjacent siblings are at x=8, x=16, x=32 indicate off-grid placement.
- Check for sub-pixel values: `absoluteBoundingBox` coordinates at `.5` increments (e.g., x=12.5) indicate a half-pixel placement. In CSS, this renders as a blurred pixel boundary on standard displays. Flag any sub-pixel bounding box coordinate.
- Compare left-edge and top-edge x/y values of elements that should be left-aligned or top-aligned. A shared left edge should produce identical `x` values in `get_metadata`. A discrepancy of 1–3px between visually-aligned siblings is an off-by-pixel drift.
- Use `get_screenshot` to visually scan for jagged edges: a row of list items where the leading icons are not vertically centered, a form layout where field labels have inconsistent left margins, or a grid of cards with mismatched top edges.
- Check auto-layout frames: if a frame uses auto-layout (`layoutMode` present in `get_metadata`), its children should not have manual position overrides. Children with `layoutPositioning: "ABSOLUTE"` inside an auto-layout frame are manually positioned exceptions — flag these if they are not intentionally floating elements.

### Common violations

- Three sibling card components in a grid have `absoluteBoundingBox.y` values of 64, 64, and 65 — the third card is 1px lower than its siblings. Auto-layout was not used, and a manual placement drifted.
- A form label has `x: 17` while the input below it has `x: 16` — a 1px left-edge misalignment not visible at glance but present in the coordinate data from `get_metadata`.
- An icon inside a button has `absoluteBoundingBox` coordinates at `x: 12.5` — a half-pixel placement that will anti-alias on standard displays.
- A table row's action icons are `absoluteBoundingBox.y`-positioned at 14, 13, 16 — three icons in the same row at three different vertical positions, indicating manual placement without vertical center alignment.

### Severity guidance

- **Minor:** Off-by-1–2px alignment on a non-interactive, non-primary element — visually subtle and low user impact → Minor.
- **Minor:** Sub-pixel (`x.5` or `y.5`) bounding box coordinate on a primary element → Minor (will render blurred on standard displays).
- **Suggestion:** Off-by-pixel on a purely decorative element (illustration, divider) with no interaction or text → Suggestion.
- **Note:** Persistent off-grid alignment across multiple sibling elements (3+) on the same row or column is a pattern, not a one-off — escalate to Major if it affects a primary surface (table, form, navigation).

## Density and breathing room

**Principle:** Primary actions and key content areas must have adequate surrounding whitespace. Crowded layouts reduce scan speed, increase error rates on touch devices, and signal a composition that has accumulated elements without systematic review. Breathing room is not decoration — it is hierarchy.

### What to look for in a Figma frame

- Call `get_metadata` for auto-layout `padding` and `itemSpacing` on frames containing primary actions (buttons, key stat cards, primary form fields). Compare against LightSpectrum spacing tokens: padding below 8px (`--spacing-2`) or gaps below 4px (`--spacing-1`) on interactive elements are likely too tight.
- Check the ratio of content area to surrounding whitespace via `absoluteBoundingBox`: if the primary action element's bounding box occupies more than ~70% of its container width, or if there is less than 8px of space between adjacent interactive elements, flag the density.
- Use `get_screenshot` as the primary signal for density: a frame that feels crowded visually — elements touching edges, no visual pause between groups, text running to within 2–4px of a border — will be immediately apparent. Confirm with `get_metadata` padding values.
- Check for stacked interaction zones: if two interactive elements (e.g., a link and a button) have `absoluteBoundingBox` values where their vertical boundaries are within 4px of each other, they are in a touch-collision zone. Flag these for density and for WCAG 2.5.8 (merge in Synthesis).
- A deliberate dense table or data grid is expected to be dense — do not flag normal row heights in data tables as a density violation. Focus on primary action areas, cards, and modals.

### Common violations

- A modal's primary CTA button has `paddingTop: 4`, `paddingBottom: 4` from `get_metadata` — the label has only 4px of vertical breathing room inside the button. The button height is visually below the minimum interactive target expectation.
- A card footer stacks "View details" (text link) and "Mark complete" (button) with `itemSpacing: 2` between them — effectively touching. Any misclick hits the wrong action.
- A form section groups five fields with `itemSpacing: 6` between them. The tightness makes it hard to scan which label belongs to which field; `get_variable_defs` confirms no spacing token binding (hardcoded 6px gap, which is not a LightSpectrum token value).
- A dashboard header packs the page title, a breadcrumb, a date filter, and three action buttons in a single row with `paddingLeft: 8` — the elements crowd the left edge and the available width is insufficient to give any element prominence.

### Severity guidance

- **Major:** Primary interactive element (button, form field, key CTA) with internal padding below 8px or external gap to an adjacent interactive element below 4px — approaches a WCAG 2.5.8 target-size violation → Major (merge with WCAG finding in Synthesis if target size also fails).
- **Minor:** Secondary content area (helper text, metadata row) is tight but not broken — density is noticeable but the task remains completable → Minor.
- **Suggestion:** Primary action area has adequate spacing but could benefit from additional breathing room to improve visual prominence without breaking function → Suggestion.

## Output template

Each finding follows the schema in [finding-model.md](finding-model.md). Set:

- `rubric: "ui-checklist"`
- `principle: "<principle name>"` (e.g., `"Visual hierarchy"` or `"Color usage — tokens vs. hardcoded"`)

Severity is assigned in Stage 3 (Synthesis) per [severity.md](severity.md), using the severity guidance in each principle's section above.
