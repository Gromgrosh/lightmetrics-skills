# Installation Guide Template

Use this template for step-by-step installation procedures, setup guides, and deployment documentation.

## Document Structure

```
1. Title & Overview
   - Document title
   - Purpose statement
   - Audience
   - Time estimate (optional)
   - Prerequisites chip list

2. Steps Section (repeat for each major step)
   - Step number and title
   - Step indicator (e.g., "STEP 01/07")
   - Purpose statement
   - Sub-steps (numbered)
     - Action description
     - Screenshot (if applicable)
     - Decision points table
   - Step completion criteria

3. General Reference (optional)
   - Common dialogs
   - Troubleshooting quick reference
   - Glossary

4. Footer
   - Version info
   - Last updated
   - Contact/support
```

## HTML Structure Pattern

### Page Hero
```html
<div class="page-hero">
  <p class="page-hero__eyebrow">[Product/App Name]</p>
  <h1 class="page-hero__title">
    <span data-lang="en">[Document Title]</span>
    <span data-lang="pt">[Portuguese Title]</span>
  </h1>
  <p class="page-hero__desc">
    <span data-lang="en">[Description]</span>
    <span data-lang="pt">[Portuguese Description]</span>
  </p>
  <div class="page-hero__chips">
    <span class="page-hero__chip">[Prerequisite 1]</span>
    <span class="page-hero__chip">[Prerequisite 2]</span>
  </div>
</div>
```

### Step Section
```html
<section class="step-section" id="step-1">
  <div class="step-section__header">
    <div class="step-section__meta">
      <span class="step-section__badge">
        <span data-lang="en">Step 1</span>
        <span data-lang="pt">Passo 1</span>
      </span>
    </div>
    <h2 class="step-section__title">
      <span data-lang="en">[Step Title]</span>
      <span data-lang="pt">[Portuguese Title]</span>
    </h2>
    <p class="step-section__indicator">
      <span data-lang="en">STEP 01/07</span>
      <span data-lang="pt">PASSO 01/07</span>
    </p>
    <p class="step-section__purpose">
      <span data-lang="en">[Purpose statement]</span>
      <span data-lang="pt">[Portuguese purpose]</span>
    </p>
  </div>

  <div class="step-section__substeps">
    <!-- Sub-steps go here -->
  </div>
</section>
```

### Sub-step with Screenshot
```html
<div class="substep" id="step-1-1">
  <div class="substep__inner substep__inner--with-screenshot">
    <div class="substep__content">
      <div class="substep__header">
        <span class="substep__badge">1.1</span>
        <h3 class="substep__title">
          <span data-lang="en">[Sub-step Title]</span>
          <span data-lang="pt">[Portuguese Title]</span>
        </h3>
      </div>
      <ol class="substep__instructions">
        <li>
          <span data-lang="en">[Instruction 1]</span>
          <span data-lang="pt">[Portuguese instruction]</span>
        </li>
        <li>
          <span data-lang="en">[Instruction 2]</span>
          <span data-lang="pt">[Portuguese instruction]</span>
        </li>
      </ol>
    </div>
    <div class="screenshot-panel">
      <img
        src="./assets/[image-name].png"
        alt="[Descriptive alt text]"
        class="screenshot-panel__img"
        loading="lazy"
      />
      <p class="screenshot-panel__caption">[Caption]</p>
    </div>
  </div>
</div>
```

### Decision Table
```html
<details class="decision-table">
  <summary class="decision-table__toggle">
    <span data-lang="en">Decision Points</span>
    <span data-lang="pt">Pontos de Decisão</span>
  </summary>
  <div class="decision-table__wrap">
    <table class="decision-table__table">
      <thead>
        <tr>
          <th><span data-lang="en">Situation</span><span data-lang="pt">Situação</span></th>
          <th><span data-lang="en">Action</span><span data-lang="pt">Ação</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>[Situation description]</td>
          <td>[Action to take]</td>
        </tr>
      </tbody>
    </table>
  </div>
</details>
```

### Callout Boxes
```html
<!-- Warning -->
<div class="callout callout--warning">
  <span class="callout__icon">⚠️</span>
  <div class="callout__body">
    <span data-lang="en">[Warning message]</span>
    <span data-lang="pt">[Portuguese warning]</span>
  </div>
</div>

<!-- Info -->
<div class="callout callout--info">
  <span class="callout__icon">ℹ️</span>
  <div class="callout__body">
    <span data-lang="en">[Info message]</span>
    <span data-lang="pt">[Portuguese info]</span>
  </div>
</div>

<!-- Conditional Step -->
<div class="callout callout--conditional">
  <span class="callout__icon">🔀</span>
  <div class="callout__body">
    <span data-lang="en">[Conditional note]</span>
    <span data-lang="pt">[Portuguese conditional]</span>
  </div>
</div>
```

## Content Guidelines

### Step Titles
- Use action verbs: "Configure", "Install", "Verify", "Connect"
- Keep concise: 2-4 words
- Match UI terminology exactly

### Instructions
- Start each instruction with an action verb
- Be specific about UI elements: "Tap **NEXT STEP**" not "proceed"
- Include conditional paths: "If X, then Y"
- Reference screenshots when helpful

### Decision Points
- Cover all common scenarios
- Include error states and recovery actions
- Link to troubleshooting where applicable

### Screenshots
- Capture the specific screen state referenced
- Use consistent device frames
- Highlight relevant UI elements if needed
- Alt text should describe the screen purpose, not just "Screenshot"

## Section Breakdown Example

For a 7-step installation guide:

| Step | Title | Sub-steps | Focus |
|------|-------|-----------|-------|
| 1 | Unboxing | 5 | Physical setup, power, connection |
| 2 | Provisioning | 1 | Device configuration state |
| 3 | Network | 3 | Connectivity verification |
| 4 | Diagnostics | 1 | Health check |
| 5 | Settings | 5 | Configuration options |
| 6 | Mounting | 8 | Physical installation |
| 7 | Complete | 1 | Final verification |
