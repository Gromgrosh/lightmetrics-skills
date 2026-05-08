# Rubric — UX writing

Source: Lightmetrics tone & voice (informed by Nielsen Norman Group's UX Writing principles, MailChimp Voice & Tone, and Microsoft's Style Guide).

## Overview

This rubric covers microcopy quality — labels, CTAs, error messages, empty states, tone, and scannability. It focuses on the *words* on the screen: whether language is clear, whether voice is consistent, whether error messages help users recover, and whether every CTA tells users exactly what will happen when they act. This is a distinct lens from the visual and interaction concerns covered by the Nielsen, Norman, WCAG, and UI-checklist rubrics.

Significant overlap exists with other rubrics at several points: Error message helpfulness shares territory with Nielsen H9 (Help users recognize, diagnose, and recover from errors) and WCAG 3.3.3 (Error suggestion); Empty-state guidance shares territory with Nielsen H10 (Help and documentation); Tone consistency overlaps with Nielsen H4 (Consistency and standards); and Microcopy labels/placeholders overlap with WCAG 1.3.1 (Info and relationships). Where the same underlying issue is flagged by multiple rubrics, the Synthesis stage merges the findings and assigns the highest severity. These overlap points are noted in the relevant sections below.

## Clarity

**Principle:** Copy must be written in plain language that any user in the target audience can understand without explanation. Jargon, internal product naming, and ambiguous phrasing slow users down and create comprehension barriers that can prevent task completion entirely.

### What to look for in a Figma frame

- Labels, headings, and button text use words that appear in everyday language, not in engineering or product-team vocabulary
- Technical terms or abbreviations that appear in the design are paired with an explanation or tooltip, or are known to be industry-standard for the target audience
- Sentences are in active voice and address the user directly where appropriate ("Your report is ready" not "Report generation has been completed")
- Section headings describe content, not actions performed by the system on data
- Error messages avoid error codes, exception class names, and internal identifiers
- Modal and dialog titles describe what the modal is for, not what triggered it

### Common violations

- ❌ "Run aggregator" as a button label → ✅ "Refresh data" — internal process name leaked into the UI.
- ❌ "NullPointerException in batch processor" as an error message → ✅ "Something went wrong — try again or contact support" — stack trace exposed in UI.
- ❌ "Entity configuration" as a form section heading → ✅ "Device settings" — engineering term used where product language is expected.
- ❌ "Provisioning failed" as a banner message → ✅ "We could not add this device — check the connection and try again" — passive, jargon-heavy message provides no actionable path.

### Severity guidance

- **Major:** Jargon or internal terminology that blocks a non-expert user from understanding what to do or what happened on a primary surface → Major. Overlaps with Nielsen H2 (Match between system and the real world) — merge in Synthesis.
- **Minor:** Slightly technical word where a plain alternative exists but comprehension is not blocked → Minor.
- **Suggestion:** Stylistic preference for simpler phrasing where current copy is clear and correct → Suggestion.

## CTA verb-orientation

**Principle:** Every button and call-to-action label must begin with an action verb that tells the user exactly what will happen when they click. Generic labels like "Submit", "OK", or "Confirm" force users to infer context; verb-first labels like "Place order", "Save changes", or "Delete account" communicate consequence and build confidence.

### What to look for in a Figma frame

- All primary and secondary button labels in the frame start with an action verb
- The verb is specific to the outcome ("Export CSV", not just "Export"; "Delete account", not "Delete")
- Confirmation dialog buttons use paired verbs that match the action and its reversal ("Delete / Keep", not "OK / Cancel")
- Link text is descriptive ("View full report", not "Click here" or "Learn more" when the destination is known)
- Icon-only buttons are out of scope for this principle (see Microcopy: labels, hints, placeholders and Norman — Signifiers)

### Common violations

- ❌ "Submit" on a checkout form → ✅ "Place order" — vague verb; user does not know what will happen.
- ❌ "OK" on a destructive confirmation dialog → ✅ "Delete report" — no indication of the consequence.
- ❌ "Confirm" on an account suspension flow → ✅ "Suspend account" — user must infer consequence from surrounding context, not from the CTA itself.
- ❌ "Yes / No" in a modal asking "Do you want to save?" → ✅ "Save changes / Discard" — monosyllabic answers require the user to re-read the question to know what each button does.
- ❌ "Click here" as link text → ✅ "View billing history" — meaningless without surrounding context; also an accessibility failure.

### Severity guidance

- **Major:** A CTA on a primary workflow surface uses a vague or non-verb label that makes the outcome unclear — users are likely to hesitate or click the wrong action → Major.
- **Minor:** A secondary or tertiary CTA uses a generic label ("OK") where context makes the meaning clear → Minor.
- **Suggestion:** A CTA label is technically a verb but could be more specific ("Send" → "Send invoice") → Suggestion.

## Error message helpfulness

*Note: This principle overlaps with Nielsen H9 (Help users recognize, diagnose, and recover from errors) and WCAG 3.3.3 (Error suggestion). When all three rubrics flag the same node for the same issue, the Synthesis stage merges them and retains the highest severity.*

**Principle:** An error message must do two things: state what went wrong, and tell the user what to do next. A message that only states the problem ("Invalid email") leaves the user to diagnose the fix themselves. A message that only offers a fix without context ("Try again") is opaque. Both parts are required for the message to be helpful.

### What to look for in a Figma frame

- Every form field that can fail has a designed error state visible in the frame or component set
- Error messages contain both a statement of the problem and a concrete next step or fix
- The fix is specific enough to act on: "Use a valid email address (example@domain.com)" rather than "Try again"
- System-level error banners name the operation that failed and suggest a recovery path
- Error messages avoid blaming the user ("You entered the wrong password" → "Password incorrect — try again or reset your password")

### Common violations

- ❌ "Invalid input" on a form field → ✅ "Enter a valid date in DD/MM/YYYY format" — states nothing about what is invalid or how to correct it.
- ❌ "Something went wrong" as a full-page error with no further guidance → ✅ "Could not load your reports — check your connection and refresh, or contact support if the problem continues" — the current message is incomplete; it states a problem without a recovery path.
- ❌ "You have entered the wrong password" → ✅ "Incorrect password — reset your password or try again" — blames the user; offers no fix.
- ❌ "Error 403" as the only text on an access-denied screen → ✅ "You do not have permission to view this page — contact your admin to request access" — exposes an HTTP code with no actionable guidance.

### Severity guidance

- **Major:** An error message states the problem but provides no fix or recovery path — users know something is wrong but not what to do → Major. Overlaps with Nielsen H9 and WCAG 3.3.3 — merge in Synthesis.
- **Blocker:** A critical form or flow has no error-state designs at all (flagged jointly with Nielsen H9 and/or Norman Feedback) → Blocker. Merge in Synthesis.
- **Minor:** Error message wording is technically complete but could be friendlier or more specific → Minor.

## Empty-state guidance

*Note: This principle overlaps with Nielsen H10 (Help and documentation). When both rubrics flag the same node, the Synthesis stage merges them.*

**Principle:** An empty state must explain why the screen or list is empty AND offer a clear next step. A bare "No data" message leaves users uncertain whether the empty state is expected, whether something has gone wrong, or what they should do to fill the screen. Empty states are often first-time-use moments — they are one of the highest-value UX writing opportunities in the product.

### What to look for in a Figma frame

- Every list, table, or data view in the frame has an empty-state variant designed
- The empty-state copy explains the cause of the empty state in plain language
- The empty-state includes a CTA, a link, or at minimum a plain-language instruction for what to do next
- Empty states for filtered/searched results explain that the filter or query returned no matches, and offer a way to clear the filter
- Empty states that result from permissions or provisioning issues explain the constraint, not just the absence

### Common violations

- ❌ "No data" in a vehicle list → ✅ "No vehicles have been added yet — add your first vehicle to start tracking" — does not explain why, and offers no next step.
- ❌ "No results found" on a search with no suggested actions → ✅ "No results for 'Depot 7' — try a different name or clear the search filter" — dead end; user must figure out next steps alone.
- ❌ "No alerts" in an alert history panel (not explained as expected or filtered) → ✅ "No alerts in the selected date range — widen the date range or check if alerts are configured" — the empty state could represent a healthy system or a misconfiguration; copy should disambiguate.
- ❌ An empty dashboard with only an illustration and no copy → ✅ Illustration + "Your dashboard is empty — create your first widget to start monitoring your fleet" — visual alone is not sufficient guidance.

### Severity guidance

- **Major:** Empty state on a primary surface shows no explanation and no next step ("No data") → Major. Overlaps with Nielsen H10 — merge in Synthesis.
- **Minor:** Empty state explains the absence but the CTA or next-step instruction is missing or vague → Minor.
- **Suggestion:** Empty state is functionally complete but could be more encouraging or specific → Suggestion.

## Tone consistency

*Note: Requires sibling context — this principle cannot be fully evaluated from a single frame in isolation. Tone consistency violations are only flaggable when two or more adjacent or sequential screens are available.*

**Principle:** The product voice must be consistent across screens. A formal, declarative tone on one screen and a warm, casual tone on the next creates a fractured experience that erodes trust. This does not require every screen to sound identical — tone can shift between contexts (an error screen can be more serious than an onboarding screen) — but the underlying voice and register must be recognisably the same product.

### What to look for in a Figma frame

- Sentence-case versus title-case style is consistent across all CTA labels, headings, and labels in the frames provided
- First- and second-person pronouns are used consistently (the product should not address the user as "you" on one screen and "the user" on another)
- Contractions are used or avoided consistently (e.g., "Don't" vs "Do not" — pick one style and apply it everywhere)
- The level of formality (imperative vs polite tone) is consistent across equivalent screen types (e.g., all confirmation dialogs should sound the same)
- Marketing/promotional copy on empty states or upsell surfaces uses a consistent register with the functional copy on nearby screens

### Common violations

- ❌ "Save Changes" (title case) on the Settings screen next to "Add new vehicle" (sentence case) on an adjacent screen → ✅ Consistent sentence case throughout — capitalization style should be decided once and applied globally.
- ❌ "We're sorry, something went wrong!" (warm, apologetic) on errors but "User not authorized." (cold, impersonal) for permission errors on the same product → ✅ Consistent empathetic but neutral tone on all error states.
- ❌ "Let's get started!" (casual, first-person plural) on onboarding and "Select a date range to proceed." (formal, imperative) on the same product's wizard → ✅ Matching register and voice.
- ❌ "You don't have any reports yet" (second-person, contraction) on one empty state and "No reports have been created." (impersonal passive) on another → ✅ Consistent second-person active voice throughout.

### Severity guidance

- **Major:** Tone clash between adjacent or sequential screens that is noticeable and jarring — a user moving through the flow would perceive the product as inconsistent → Major. Requires sibling context to flag; overlaps with Nielsen H4 (Consistency and standards) — merge in Synthesis.
- **Minor:** Capitalization inconsistency (title case vs sentence case) within one screen or between very similar screens → Minor.
- **Suggestion:** Tone preference (warmer vs cooler, more vs less formal) where the current voice is consistent but could be improved → Suggestion.

## Length and scannability

**Principle:** Users scan interfaces; they do not read them. Copy must be as short as it can be without losing meaning. Long sentences, redundant phrases, and unnecessary preamble increase cognitive load and delay action. Where three words will do, do not use eight.

### What to look for in a Figma frame

- Button labels and CTAs are one to four words
- Form field labels are short and noun-form ("Full name", not "Please enter your full name")
- Paragraph copy in tooltips, empty states, and inline help fits within 2–3 short sentences
- Instructional copy does not repeat information already communicated by the heading or context
- Modal body copy does not restate the modal title
- Long body copy uses bullets or short paragraphs rather than continuous prose where items are enumerable

### Common violations

- ❌ "Please click the button below to save all of your changes and continue to the next step" → ✅ "Save and continue" — the button label contains all the necessary information; the surrounding copy is redundant.
- ❌ "In order to be able to use this feature, you will first need to configure your account settings." → ✅ "To use this feature, configure your account settings first." — filler phrases ("In order to be able to") add length without adding meaning.
- ❌ A tooltip that is four sentences long and repeats the label it is attached to → ✅ One sentence stating the purpose and one sentence for any constraint or example — tooltips should supplement, not restate.
- ❌ Modal body: "Are you sure you want to delete this report? This action is permanent and cannot be reversed. If you delete this report, you will not be able to recover it." → ✅ "This will permanently delete the report. You cannot undo this action." — three sentences saying the same thing, collapsed to two.

### Severity guidance

- **Minor:** Copy is verbose or repetitive but is correct and does not mislead — a user can still complete the task → Minor.
- **Suggestion:** Copy is marginally long or could be tightened by preference, but is not meaningfully worse than the concise alternative → Suggestion.

## Correctness

**Principle:** Copy must be factually accurate and must not mislead the user about the product's behavior, pricing, legal standing, or consequences of actions. Incorrect or misleading copy can cause real harm — a user who deletes data because a button was labeled "Archive" has been misled by the design. This is the highest-stakes writing concern.

### What to look for in a Figma frame

- CTA labels accurately describe what will happen (a button that deletes data must not say "Remove" if removal is recoverable but deletion is not)
- Pricing, unit, and currency information in the design matches the product's documented pricing (flag if there is reason to suspect a mismatch)
- Legal disclaimers, consent copy, and terms references are present where the flow requires them
- Feature capability claims in empty states and marketing copy match the product's documented capabilities
- Date, time, and unit formats are unambiguous (e.g., "01/02/03" is ambiguous — prefer ISO 8601 or spelled-out month names)

### Common violations

- ❌ "Archive" on a button that permanently deletes data → ✅ "Delete permanently" — "archive" implies reversibility; if the action is destructive, the label must say so.
- ❌ "Cancel" as a button that submits a cancellation request (and is therefore a positive action) next to "Back" → ✅ "Cancel subscription" for the destructive action, "Keep subscription" for the cancel — "Cancel" is ambiguous in this context and can cause users to trigger the opposite of their intent.
- ❌ "Free forever" in a feature upsell that is actually part of a trial period → ✅ "Free during your trial" — copy that misrepresents the product's pricing is a Blocker.
- ❌ "02/03/04" as a displayed date → ✅ "2 March 2004" or "2004-03-02" — ambiguous date format where locale interpretation is not guaranteed.

### Severity guidance

- **Blocker:** Copy is factually wrong or actively misleads the user about the consequence of an action, about pricing, or about product capability in a way that could cause harm or erroneous action → Blocker (per severity.md: misleading or wrong copy).
- **Major:** Copy is ambiguous in a way that is likely to cause a significant portion of users to make the wrong choice (e.g., "Cancel" in a dual-button confirmation context) → Major.
- **Minor:** Copy is technically imprecise but not misleading and does not affect action outcomes → Minor.

## Microcopy: labels, hints, placeholders

*Note: The use of a placeholder as the only label for an input (no visible label element) is an accessibility failure and overlaps with WCAG 1.3.1 (Info and relationships) — merge in Synthesis.*

**Principle:** Form labels, input hints, and placeholder text are the primary tools users rely on to understand what a field requires. Labels must describe the input clearly and remain visible at all times. Hints should clarify format or constraint. Placeholders should supplement — never replace — the label, and should hint at format or example rather than repeat the label text.

### What to look for in a Figma frame

- Every input field has a visible, persistent label (not only a placeholder)
- Labels use noun form and are left-aligned above or beside the field ("Full name", not "Enter full name here")
- Placeholder text (when present) gives an example value or format hint, not a restatement of the label
- Helper/hint text beneath an input explains constraints or format (e.g., "Password must be at least 8 characters")
- Required fields are marked consistently (asterisk + legend, or "Required" text)
- Optional fields are marked when most fields in a form are required (to reduce cognitive overhead)
- Character count indicators are present where fields have a limit

### Common violations

- ❌ An email field with only placeholder "Enter your email" and no visible label → ✅ A label "Email" above the field, with placeholder "name@company.com" — placeholder-only labeling violates WCAG 1.3.1; merge in Synthesis.
- ❌ Placeholder text "Password" in a password field → ✅ Label "Password" above the field; placeholder "At least 8 characters" (format hint) — the placeholder is repeating the label rather than supplementing it.
- ❌ "Enter text" as placeholder in a search field → ✅ "Search vehicles by name or ID" — generic placeholder that does not communicate the scope or expected input.
- ❌ Required fields marked with asterisks but no legend explaining what * means → ✅ Asterisk legend ("* Required") present near the top of the form — unmarked convention creates ambiguity for first-time users.
- ❌ A 140-character bio field with no character count indicator → ✅ Character count ("0 / 140") visible beneath the field — without feedback, users will exceed limits and receive an error they could have avoided.

### Severity guidance

- **Major:** An input field has no visible label at all — placeholder is the only labeling → Major. Overlaps with WCAG 1.3.1 (Info and relationships) — merge in Synthesis and assign Blocker if the field is on a primary task flow (WCAG AA failure).
- **Major:** A required field is not marked as required, and its absence is not obvious from context → Major.
- **Minor:** Placeholder text repeats the label rather than adding a hint — label is present and accessible → Minor.
- **Minor:** Helper text is absent for a field with a non-obvious constraint (e.g., a phone number field that accepts only one format) → Minor.
- **Suggestion:** An optional field is not marked optional — would reduce user uncertainty but is not a blocker → Suggestion.

## Output template

Each finding follows the schema in [finding-model.md](finding-model.md). Set:

- `rubric: "ux-writing"`
- `principle: "<principle name>"` (e.g., `"CTA verb-orientation"`, `"Error message helpfulness"`, `"Microcopy: labels, hints, placeholders"`)

Severity is assigned in Stage 3 (Synthesis) per [severity.md](severity.md), using the severity guidance in each principle's section above. Where a UX writing finding duplicates a Nielsen, WCAG, or Norman finding on the same node and issue, the Synthesis stage merges them and retains the higher severity.
