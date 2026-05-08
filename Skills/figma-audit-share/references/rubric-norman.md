# Rubric — Don Norman's design principles

Source: Don Norman, *The Design of Everyday Things* (revised 2013).

## Overview

Apply each of Norman's 8 design principles to the target node and its sibling context (if available). Emit a finding per principle violation, following the schema in [finding-model.md](finding-model.md).

This rubric complements the Nielsen heuristics rubric. The Norman lens emphasises the *physical and perceptual* qualities of a design — whether controls are visually findable, whether interactive elements signal how they work (affordances and signifiers), whether the layout communicates the right mental model, and whether the design prevents invalid use by construction. Nielsen and Norman share territory at several points (Visibility ↔ H1, Feedback ↔ H1/H9, Consistency ↔ H4); these overlaps are noted in each relevant principle's guidance section so the Synthesis stage can merge duplicate findings rather than report them twice.

## Visibility

**Principle:** Important controls and status information must be perceptually available to the user — they should not need to hunt, hover, or scroll to discover what actions are possible or what state the system is in.

### What to look for in a Figma frame
- Primary actions are in the visible viewport of the frame, not below the fold or behind a secondary control
- Controls that affect the current view (filters, sort, bulk-select) are placed near the content they affect
- State changes — active, selected, current — are visually encoded on the element itself, not only in a remote status area
- Navigation items indicate where the user is (current-page affordance visible without hover)
- Destructive or irreversible actions are not hidden behind unlabelled icon menus without any surface-level hint
- Secondary controls that are contextually relevant to the task do not require expanding or revealing panels to discover

### Common violations
- A bulk-action toolbar appears only after rows are selected, with no placeholder or hint that bulk actions exist in the default (zero-selection) state — users who do not know to look will not find the feature.
- A primary CTA ("Place order") is positioned below a long scroll with no sticky affordance, making it invisible at the default viewport.
- The currently active navigation section is indicated only by a slight colour shift that does not distinguish it clearly from hover, leaving users uncertain where they are.
- A destructive action ("Archive workspace") is placed three levels deep in an overflow menu with no surface-level warning, making the risk invisible until it is too late.

### Severity guidance
- **Major:** A primary interactive control needed to complete the current task is not visible in the default viewport of the frame with no affordance or hint to its existence → Major. Overlaps with Nielsen H1 (Visibility of system status) and H6 (Recognition rather than recall) — merge in Synthesis.
- **Major:** Navigation or state information that the user needs to orient themselves is absent from the visible frame → Major.
- **Minor:** A secondary feature or shortcut is not surfaced but a reasonable user would eventually find it → Minor.
- **Suggestion:** A rarely-used control is hidden but the hiding is intentional progressive disclosure → Suggestion.

## Feedback

**Principle:** Every action must produce a clear, immediate, perceptible response so the user knows the system received the action and understands the result.

### What to look for in a Figma frame
- Every interactive element (button, toggle, link, form submission) has at least one non-default state that represents a response (loading, success, error, changed)
- Loading or processing states are designed for operations that take time (file upload, data query, payment processing)
- Success states confirm completion (not just returning to default)
- Error states are attached to the triggering control or field, not only a remote banner
- Toggle and checkbox states are unambiguous — on/off, checked/unchecked are visually distinct even in isolation

### Common violations
- A "Save" button has Default and Disabled variants but no Loading or Success state — after clicking, the user cannot tell whether the save was received.
- A file-upload component shows no progress indicator — once the user drops a file, the design returns to an idle appearance with no acknowledgement.
- A destructive action (e.g., "Delete report") transitions immediately to the next screen in the design with no confirmation or undo affordance — the feedback that the action completed is the disappearance of the item, with no explicit message.
- A form submission error is displayed in a page-level banner at the top, but the form fields below show no in-context error state — users must read the banner to know which field failed.

### Severity guidance
- **Blocker:** A primary action (form submit, destructive delete, payment confirm) has no feedback state at all — the user cannot tell if the system received the action → Blocker. Overlaps with Nielsen H1; merge in Synthesis.
- **Major:** A time-consuming operation (upload, data processing, report generation) has no loading state design → Major.
- **Minor:** A secondary, non-critical action (e.g., a filter clear) has no explicit confirmation feedback but a page-level state change implies success → Minor.

## Affordances

**Principle:** The visual properties of an element should suggest, without instruction, how it is meant to be used — buttons look pressable, sliders look draggable, links look clickable.

### What to look for in a Figma frame
- Buttons have visual depth cues (fill, border, shadow, or a combination) that distinguish them from static containers
- Interactive text (links) are differentiated from non-interactive body text by colour and/or underline
- Draggable elements (cards, rows, panels) have a visual handle or grip cue
- Sliders, scrollbars, and range inputs have a thumb shape that looks movable
- Clickable image thumbnails or cards have a hover-state variant or border/shadow that signals interactivity
- Flat/ghost buttons are sufficiently distinct from static labels — a ghost button with only a text label and a border that matches body-text colour reads as a label

### Common violations
- A primary CTA is styled with a flat, low-contrast fill and no border or shadow — it visually reads as a section header rather than a pressable control.
- Inline text links in a paragraph are the same colour as the surrounding body text, differentiated only by bold weight — most users will not perceive them as clickable.
- A drag-and-drop list has no grip icon or drag handle on the row — users have no visual cue that reordering is possible.
- A clickable card has no border, shadow, or visible interactive state in the Figma frame — the card reads as static content.

### Severity guidance
- **Blocker:** A primary interactive element does not visually differentiate from static content to the degree that users are likely to not attempt to interact with it at all → Blocker (primary task broken, per severity.md).
- **Major:** A button or link does not clearly read as interactive — a reasonable user is likely to overlook it or mistake it for a label → Major.
- **Minor:** A secondary interactive element (e.g., a tertiary action) has weak affordance but the task is still completable via an alternative path → Minor.
- **Suggestion:** An affordance cue could be strengthened (e.g., adding a subtle shadow to an already-recognisable button) → Suggestion.

## Signifiers

**Principle:** Explicit perceptual signals — labels, icons paired with labels, tooltips, placeholder text — must communicate what actions are available and what each control does. Signifiers make affordances discoverable.

### What to look for in a Figma frame
- Icon-only buttons have a visible label or a designed tooltip variant in the component set — icon alone is insufficient unless the icon is universally understood (e.g., a filled-star for "favourite")
- Placeholder text in form inputs hints at the required format or an example value
- Action buttons use verb labels ("Save", "Delete", "Export") rather than ambiguous nouns ("Data", "Settings")
- Segmented controls and tab bars label every segment — no segments that rely on icon-only without a text label
- Overlay or popover triggers (info icons, help icons, expand icons) are visually signified so users know something will appear
- Empty states include a signifier for the next action ("Create your first report" with a CTA) rather than displaying only a negative message ("No data found")

### Common violations
- A toolbar contains six icon-only buttons (export, filter, refresh, share, print, delete) with no labels and no tooltip variant in the design — users must guess each action from the icon alone.
- A segmented toggle uses icons only (list-view icon vs. grid-view icon) with no text label — users unfamiliar with the product will not immediately understand what each mode does.
- An "i" info icon has no tooltip or popover state variant designed — the signifier (the icon) exists but the content it signals is never shown.
- A date picker input shows no placeholder format hint (e.g., "DD/MM/YYYY") — users do not know which date format is expected.

### Severity guidance
- **Major:** An icon-only button on a primary workflow surface that users must interact with to complete their task, and no label or tooltip variant exists in the component set → Major. Consider context: a universally understood icon (trash, close ×) in a well-established position is more defensible than a custom icon.
- **Minor:** Icon-only button in a secondary or power-user context where users are expected to learn the interface → Minor.
- **Minor:** Missing format hint on a form field that has inline validation and a clear error message designed → Minor.
- **Suggestion:** An info icon exists but its tooltip content is not mocked in the design — functionality is signified but content is unspecified → Suggestion.

## Mapping

**Principle:** The spatial and visual relationship between a control and its effect must match the user's expectations — toggles should clearly indicate which state is "on", grouped controls should affect only their grouped content, and layout should reflect the mental model of the system.

### What to look for in a Figma frame
- Toggle switches have a visible "on" and "off" direction that matches convention (right = on, left = off in LTR layouts) and a label that names the state, not the action
- Toggle labels describe the current state ("Notifications enabled") rather than the toggle's action ("Enable notifications") — the latter creates ambiguity about whether the current state is active or inactive
- Form controls are visually proximate to the content they affect — a filter panel is adjacent to or overlaps the filtered content, not positioned on the opposite side of the screen
- Stepper controls (quantity, pagination) use + on the right and − on the left, matching the directional expectation for increase/decrease
- Tab navigation order matches the logical task sequence
- Grouped options (radio buttons, checkboxes) are spatially grouped with their group label, not interleaved with other groups

### Common violations
- A toggle is labelled "Show advanced options" — when the toggle is on, is the user showing or hiding? The label does not clearly communicate current state vs. intended action.
- A filter sidebar physically positioned to the right of a results list creates a right-to-left causal flow (filter → results) that opposes the natural reading direction in LTR interfaces.
- A settings panel has a "Save changes" button at the top of the form, above all the fields — spatial mapping places the outcome before the inputs.
- A quantity stepper shows "–" on the right and "+" on the left, reversing the directional convention for increase.

### Severity guidance
- **Major:** A toggle or binary control's label or direction is ambiguous or contradicts convention such that users are likely to set the wrong state → Major. This is distinct from Nielsen H4 (Consistency) — the concern here is control–effect mapping, not cross-screen consistency.
- **Major:** Spatial layout places a control far from the content it affects, requiring users to infer a non-obvious relationship → Major.
- **Minor:** A label reads as an action ("Enable X") rather than a state ("X enabled") but the toggle direction is correct and conventional → Minor.
- **Suggestion:** A grouping or ordering of controls could better reflect the task sequence but the current arrangement is not confusing → Suggestion.

## Constraints

**Principle:** The design should prevent invalid or dangerous actions from being performed by making them impossible or by making their inadvisability visible — through disabled states, mutually exclusive option controls, confirmation steps, and contextual disabling.

### What to look for in a Figma frame
- Mutually exclusive options use radio buttons (or a segmented control) rather than checkboxes — checkboxes imply independent, non-exclusive selection
- A submit or confirm button is in a disabled state (or visually suppressed) when required fields are empty or preconditions are not met
- Destructive actions (delete, archive, revoke) have a confirmation step designed, not a single-click execution
- Form fields that accept only a specific range or format have input constraints visible in the design (e.g., a date range picker enforces that End ≥ Start; a number input has min/max boundaries communicated)
- Options that are unavailable in the current context are shown as disabled rather than hidden — hiding removes the signifier that the option exists

### Common violations
- A "Delete account" button is fully enabled on a page with no confirmation step or two-step verification designed — the constraint against accidental deletion is absent.
- A form with three required fields has a fully-active "Submit" button regardless of whether any fields are filled — no constraint prevents a failed submission.
- A date-range picker allows an End date earlier than the Start date to be selected — the invalid state is not constrained in the design.
- A multi-select list and a "Select all" checkbox coexist alongside a set of mutually exclusive single-select options — the control type does not communicate the exclusivity constraint.

### Severity guidance
- **Blocker:** Destructive or irreversible action with no confirmation step and no constraint preventing accidental execution → Blocker (critical interaction state missing, per severity.md).
- **Major:** A submit action is enabled when preconditions are clearly not met (e.g., empty required fields) — users will trigger an error state that could have been prevented by design → Major.
- **Major:** Mutually exclusive options are presented with checkboxes instead of radio buttons, actively allowing invalid multi-selection → Major.
- **Minor:** An unavailable option is hidden rather than disabled — users cannot tell the option exists → Minor.
- **Suggestion:** A form could be improved by proactive inline validation (e.g., real-time password strength) but the absence is not an error → Suggestion.

## Consistency

**Principle:** The same visual language, interaction patterns, and terminology must be used throughout the design so that learning generalises across screens.

*Note: This principle overlaps substantially with Nielsen H4 (Consistency and standards). When both rubrics flag the same finding, the Synthesis stage should merge them and assign the higher severity. The Norman lens here is narrower — it focuses on whether the design communicates a coherent internal model, rather than conformance to external platform conventions.*

### What to look for in a Figma frame
- Primary buttons use the same visual style across all frames provided (fill, radius, type style)
- The same action always uses the same label — cross-screen comparison required if sibling context is available
- Icon usage is internally consistent — the same icon maps to the same action everywhere in the design
- Form field styles (border, radius, padding, label position) are uniform across the design
- Error state styling is uniform across all form fields
- Spacing and layout grid appear consistent across equivalent sections and screens

### Common violations
- A "Save" button uses a filled primary style on the Settings screen but an outlined secondary style on the Profile screen — users cannot build a reliable model of button hierarchy.
- The trash icon is used for "delete" on the Users table but used for "remove from list" (a non-destructive action) on the Dashboard — the same icon maps to different consequence levels.
- Form fields on the Login screen have 8px border-radius but form fields on the Onboarding screen have 4px — no apparent reason for the discrepancy.
- The navigation labels change terminology between screens: "Reports" in the sidebar becomes "Analytics" in the breadcrumb of the reports page.

### Severity guidance
- **Major:** Cross-screen inconsistency in primary action styling or labelling that would prevent users from building a reliable interaction model → Major. This overlaps with Nielsen H4; merge in Synthesis and assign the higher severity.
- **Minor:** Single-screen inconsistency (e.g., one button styled differently from its peers on the same screen) → Minor.
- **Suggestion:** A stylistic variation that is not part of the established LightSpectrum pattern but does not break usability → Suggestion.

## Conceptual model

**Principle:** The design must communicate a clear and accurate mental model of how the system works — the user's understanding of what the product is and what each control does should closely match reality. When the design's appearance implies a model that contradicts actual system behaviour, errors and frustration follow.

### What to look for in a Figma frame
- The information architecture visible in the frame (navigation labels, section headings, page structure) maps to an understandable hierarchy
- Metaphors used in the design (icons, illustrations, naming) are accurate — a "folder" icon on an action that does not actually create a folder breaks the model
- System capabilities and limits are communicated proactively (e.g., if a table supports a maximum of 1000 rows, this is signalled in the empty state or onboarding, not only at overflow time)
- Multi-step flows communicate the complete model before the user commits (e.g., a checkout flow that shows the number of steps and their names before the user starts)
- Settings panels group controls in a way that matches the user's conceptual grouping, not the engineering implementation grouping
- Labels use the user's vocabulary for the task domain, not the product team's internal naming

### Common violations
- A feature called "Workspaces" in the navigation is exposed as "Projects" in the breadcrumb and "Environments" in the settings panel — three names for the same concept create a fragmented conceptual model.
- A toggle labelled "Live mode" in the design implies a real-time data feed, but the underlying system batches updates every 15 minutes — the design communicates a false model.
- A drag-to-reorder list uses a save button at the bottom, implying the reorder is not live — if the system actually saves on drop, the button misleads the model.
- A "Templates" section in the navigation contains both user-created templates and system defaults with no visual distinction — users cannot build an accurate model of what they own vs. what the system provides.

### Severity guidance
- **Major:** Terminology or metaphor used in the design contradicts or materially misrepresents the actual system behaviour in a way that is likely to cause user error → Major. Requires design context or annotation to confirm — flag with confidence `likely` when inferred from the frame alone.
- **Minor:** Information architecture grouping is non-obvious but not actively misleading — a user would adapt after brief exploration → Minor.
- **Suggestion:** A conceptual-model concern that is inferential or subjective, where reasonable designers could disagree about whether the implied model is misleading → Suggestion, confidence: `suggestion`. Conceptual model violations are often of this type; bias toward Suggestion unless a concrete, demonstrable mismatch is present.

## Output template

Each finding follows the schema in [finding-model.md](finding-model.md). Set:

- `rubric: "norman"`
- `principle: "<principle name>"` (e.g., `"Affordances"`, `"Mapping"`, `"Conceptual model"`)

Severity is assigned in Stage 3 (Synthesis) per [severity.md](severity.md), using the severity guidance in each principle's section above. Where a Norman finding duplicates a Nielsen finding on the same node and issue, the Synthesis stage merges them and retains the higher severity.
