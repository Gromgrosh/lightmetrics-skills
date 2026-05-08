# Rubric — Nielsen's 10 usability heuristics

Source: Jakob Nielsen, "10 Usability Heuristics for User Interface Design" (Nielsen Norman Group, 1994; updated 2024).

## Overview

Apply each of the 10 heuristics to the target node and its sibling context (if available). Emit a finding per principle violation, following the schema in [finding-model.md](finding-model.md).

## H1: Visibility of system status

**Principle:** The design should always keep users informed about what is going on, through appropriate feedback within reasonable time.

### What to look for in a Figma frame
- Loading indicators present for any operation that takes time
- Progress indicators on multi-step flows (current step labeled)
- Disabled vs. active state distinguishable
- Notifications/toasts visible
- Selected items visually distinct from unselected
- Active navigation item highlighted

### Common violations
- Submit button has no loading state design
- Multi-step form lacks "Step X of Y" affordance
- Disabled states are not visually distinct (just slightly faded)

### Severity guidance
- **Blocker:** A primary action with no feedback state at all (the user can't tell if the system is responding) → Blocker.
- **Major:** A multi-step flow with no progress indicator → Major.
- **Minor:** Disabled states styled inconsistently across the screen → Minor.

## H2: Match between system and the real world

**Principle:** The design should speak the users' language, with words, phrases, and concepts familiar to the user, rather than internal jargon.

### What to look for in a Figma frame
- Labels use plain language, not internal product terms
- Icons match commonly understood metaphors
- Error messages don't reference internal codes
- Date/number formats match user locale conventions

### Common violations
- "401" displayed instead of "Sign in to continue"
- Internal product naming leaked into UI ("Run aggregator")
- Industry jargon in user-facing copy

### Severity guidance
- **Blocker:** Critical copy uses jargon that prevents task completion → Blocker.
- **Major:** Labels use internal product naming → Major.
- **Minor:** Slightly technical word where a simpler alternative exists → Minor.

## H3: User control and freedom

**Principle:** Users often perform actions by mistake. They need a clearly marked "emergency exit" to leave the unwanted state.

### What to look for in a Figma frame
- Cancel/Back affordance on every modal, dialog, full-screen flow
- Undo for destructive actions
- "Are you sure?" confirmation on destructive actions
- Escape route from any deep flow

### Common violations
- Modal with no close button (X)
- Multi-step flow with no Back button
- Destructive action (Delete) with no confirmation step

### Severity guidance
- **Blocker:** Destructive action with no confirmation AND no undo → Blocker.
- **Major:** Modal with no clear way to dismiss → Major.

## H4: Consistency and standards

**Principle:** Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow platform and industry conventions.

### What to look for in a Figma frame
- Same actions use same labels across screens (sibling context required)
- Primary buttons styled consistently
- Iconography consistent (same icon = same action)
- Capitalization style consistent (sentence case vs. title case)
- Layout patterns consistent (form labels above vs. beside inputs — pick one)

### Common violations
- "Sign in" on one screen, "Log in" on another
- Primary CTA filled blue on screen A, outline blue on screen B
- Icon for "delete" used to mean "close" elsewhere

### Severity guidance
- **Major:** Cross-screen inconsistency in primary action labels or styling (requires sibling context).
- **Minor:** Single-screen capitalization inconsistency.
- **Suggestion:** Iconography choice that could be more conventional.

## H5: Error prevention

**Principle:** Good error messages are important, but the best designs carefully prevent problems from occurring in the first place.

### What to look for in a Figma frame
- Required fields marked clearly
- Format hints inline (e.g., "Use YYYY-MM-DD")
- Confirmation step on irreversible actions
- Disabled submit until form is valid (or clear validation feedback)
- Defaults that prevent common mistakes

### Common violations
- "Delete account" with no confirmation typing required
- Date input with no format hint, no datepicker
- Form submits to error state instead of validating inline

### Severity guidance
- **Blocker:** Irreversible destructive action with no error-prevention design → Blocker.
- **Major:** Form with no inline validation design → Major.

## H6: Recognition rather than recall

**Principle:** Minimize the user's memory load by making elements, actions, and options visible.

### What to look for in a Figma frame
- Recently used items surfaced (history, recents)
- Important info on screen, not hidden behind clicks
- Form fields show what was previously entered (autofill, persistence)
- Selected filters visible, not hidden in a menu

### Common violations
- Multi-step form requires user to remember earlier inputs (no review screen)
- Search lacks recent-search suggestions
- Filter selections hidden in a collapsed panel

### Severity guidance
- **Major:** Multi-step flow with no review/summary screen → Major.
- **Minor:** Recently-used affordance missing where it would help → Minor.

## H7: Flexibility and efficiency of use

**Principle:** Shortcuts — hidden from novice users — may speed up the interaction for the expert user.

### What to look for in a Figma frame
- Keyboard shortcuts documented (in tooltips or a shortcuts panel)
- Bulk actions available where applicable (multi-select, batch operations)
- Customizable views/saved filters

### Common violations
- Power-user table with no bulk-action affordance
- Repetitive task with no shortcut path

### Severity guidance
- **Major:** Power-user surface (admin, settings) with no efficiency affordances → Major.
- **Minor:** Common keyboard shortcut not documented in UI → Minor.
- **Suggestion:** Could benefit from a saved-filter mechanism → Suggestion.

## H8: Aesthetic and minimalist design

**Principle:** Interfaces should not contain information which is irrelevant or rarely needed.

### What to look for in a Figma frame
- Visual noise (excessive borders, dividers, decorative elements without purpose)
- Density: enough breathing room around primary actions
- Information hierarchy clear (one primary action, not five)
- No competing CTAs

### Common violations
- Three buttons of equal weight on one screen
- Heavy use of dividers/borders that fragment the layout
- Decorative imagery competing with primary content

### Severity guidance
- **Major:** Multiple competing primary CTAs (no clear hierarchy) → Major.
- **Minor:** Excessive dividers fragmenting the layout → Minor.
- **Suggestion:** Decorative element that could be removed → Suggestion.

## H9: Help users recognize, diagnose, and recover from errors

**Principle:** Error messages should be expressed in plain language, precisely indicate the problem, and constructively suggest a solution.

### What to look for in a Figma frame
- Error states designed for every form field that can fail
- Error message states the problem AND offers a fix
- Errors visually distinct (color + icon, not just color)
- Errors anchored to the field/action that triggered them

### Common violations
- "Invalid input" — no indication of what's wrong or how to fix
- Error message in a banner with no anchor to the failing field
- Error states colored only with red (color-only signal)

### Severity guidance
- **Blocker:** Form with no error-state designs at all → Blocker.
- **Major:** Error message that states problem but offers no fix → Major.
- **Minor:** Error visually relies on color alone (no icon or text marker) → Minor (overlaps with WCAG 1.4.1; merge in Synthesis).

## H10: Help and documentation

**Principle:** It's best if the system doesn't need any explanation. However, it may be necessary to provide documentation to help users understand how to complete tasks.

### What to look for in a Figma frame
- Inline help where tasks are non-obvious (info icons, tooltips)
- Empty states with guidance (not just "No data")
- First-time-user onboarding affordances
- Documentation links where relevant

### Common violations
- Empty state that says "No data" with no next-step guidance
- Complex feature with no inline explanation
- Onboarding skipped entirely

### Severity guidance
- **Major:** Empty state with no guidance on a primary surface → Major.
- **Minor:** Complex feature missing an info-icon explanation → Minor.

## Output template

Each finding follows the schema in [finding-model.md](finding-model.md). Set:

- `rubric: "nielsen"`
- `principle: "H<N>: <name>"` (e.g., `"H4: Consistency and standards"`)

Severity is assigned in Stage 3 (Synthesis) per [severity.md](severity.md), using the severity guidance in each principle's section above.
