# Installation Guide Template

Use this template for step-by-step installation procedures, setup guides, and deployment documentation.

> **Note**: This template follows the [Common Template Specification](./common-template-spec.md) for header, sidebar, hero, and image handling.

## Document Structure

```
1. Header (from common spec)
   - Logo + document name + platform
   - Language selector
   - Hamburger menu (tablet/mobile)
   - Progress bar

2. Side Panel (from common spec)
   - Section title ("INSTALLATION STEPS")
   - Numbered items with descriptions
   - Back to top link
   - Document date

3. Hero Section
   - Platform eyebrow
   - Document title
   - Description paragraph

4. Steps Section (repeat for each major step)
   - Step badge and title
   - Step indicator (e.g., "STEP 01/07") — optional
   - Purpose statement
   - Sub-steps with:
     - Subsection badge + title
     - Instructions (numbered list)
     - Images in tinted containers

5. Footer
   - Version info
   - Last updated
   - Contact/support
```

## HTML Structure Pattern

### Complete Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Document Title] — [Platform]</title>
  <link rel="stylesheet" href="./styles.css">
</head>
<body data-lang="en">

  <!-- Header with progress bar -->
  <header class="site-header">
    <a href="#" class="site-header__brand">
      <img src="./assets/lightmetrics-logo.svg" alt="Lightmetrics" class="brand-logo-img" />
      <span class="brand-divider"></span>
      <span class="brand-text">
        <span class="brand-name">[Document Name]</span>
        <span class="brand-sub">[Platform/App Name]</span>
      </span>
    </a>

    <div class="lang-selector">
      <select class="lang-selector__dropdown" id="langSelect">
        <option value="en">English</option>
        <option value="pt">Português</option>
      </select>
    </div>

    <button class="hamburger" id="menuToggle" aria-label="Toggle menu">
      <span></span>
      <span></span>
      <span></span>
    </button>
  </header>

  <!-- Progress Bar -->
  <div class="progress-bar">
    <div class="progress-bar__fill" id="progressFill"></div>
  </div>

  <!-- Sidebar Overlay -->
  <div class="sidebar-overlay" id="sidebarOverlay"></div>

  <!-- Side Panel -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar__head">
      <span>INSTALLATION STEPS</span>
      <button class="sidebar__close" id="sidebarClose" aria-label="Close menu">✕</button>
    </div>

    <ul class="sidebar__list">
      <li>
        <a href="#step-1" class="sidebar__link">
          <span class="sidebar__num">1</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Unboxing</span>
            <span class="sidebar__subtitle">5 sub-steps</span>
          </span>
        </a>
      </li>
      <!-- Repeat for each step -->
    </ul>

    <div class="sidebar__foot">
      <a href="#top" class="sidebar__back-to-top">↑ Back to top</a>
      <p class="sidebar__date">Last updated: [Date]</p>
    </div>
  </aside>

  <!-- Main Content -->
  <div class="app-layout">
    <main class="app-content" id="top">
      <!-- Hero Section -->
      <!-- Step Sections -->
    </main>
  </div>

  <script src="./scripts.js"></script>
</body>
</html>
```

### Hero Section

```html
<div class="page-hero">
  <p class="page-hero__eyebrow">
    <span data-lang="en">[PLATFORM NAME]</span>
    <span data-lang="pt">[NOME DA PLATAFORMA]</span>
  </p>
  <h1 class="page-hero__title">
    <span data-lang="en">[Document Title]</span>
    <span data-lang="pt">[Título do Documento]</span>
  </h1>
  <p class="page-hero__desc">
    <span data-lang="en">[Description paragraph explaining the purpose and audience]</span>
    <span data-lang="pt">[Parágrafo de descrição]</span>
  </p>
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
      <!-- Optional: Conditional badge -->
      <!-- <span class="step-section__conditional">Conditional</span> -->
    </div>
    <h2 class="step-section__title">
      <span data-lang="en">[Step Title]</span>
      <span data-lang="pt">[Título do Passo]</span>
    </h2>
    <!-- Optional: Step indicator -->
    <p class="step-section__indicator">
      <span data-lang="en">STEP 01/07</span>
      <span data-lang="pt">PASSO 01/07</span>
    </p>
    <p class="step-section__purpose">
      <span data-lang="en">[Purpose statement explaining what this step accomplishes]</span>
      <span data-lang="pt">[Declaração de propósito]</span>
    </p>
  </div>

  <div class="step-section__substeps">
    <!-- Sub-steps go here -->
  </div>
</section>
```

### Sub-step with Image

Instructions can come **before** or **after** images. Images should be in tinted containers.

```html
<div class="substep" id="step-1-1">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">1.0</span>
      <h3 class="substep__title">
        <span data-lang="en">[Subsection Title]</span>
        <span data-lang="pt">[Título da Subseção]</span>
      </h3>
    </div>

    <ol class="substep__instructions">
      <li>
        <span data-lang="en">[Instruction 1]</span>
        <span data-lang="pt">[Instrução 1]</span>
      </li>
      <li>
        <span data-lang="en">[Instruction 2]</span>
        <span data-lang="pt">[Instrução 2]</span>
      </li>
    </ol>

    <!-- Image in tinted container (NOT clickable) -->
    <figure class="image-container">
      <img
        src="./assets/[image-name].png"
        alt="[Descriptive alt text]"
        loading="lazy"
      />
    </figure>

    <!-- Additional instructions can follow the image -->
    <ol class="substep__instructions" start="3">
      <li>
        <span data-lang="en">[Instruction 3]</span>
        <span data-lang="pt">[Instrução 3]</span>
      </li>
    </ol>
  </div>
</div>
```

### Sub-step with Inline Screenshot (side-by-side layout)

For smaller screenshots that appear beside instructions:

```html
<div class="substep" id="step-1-2">
  <div class="substep__inner substep__inner--with-screenshot">
    <div class="substep__content">
      <div class="substep__header">
        <span class="substep__badge">1.1</span>
        <h3 class="substep__title">
          <span data-lang="en">[Subsection Title]</span>
          <span data-lang="pt">[Título da Subseção]</span>
        </h3>
      </div>
      <ol class="substep__instructions">
        <li>
          <span data-lang="en">[Instruction 1]</span>
          <span data-lang="pt">[Instrução 1]</span>
        </li>
      </ol>
    </div>
    <div class="screenshot-panel">
      <div class="screenshot-panel__wrap">
        <img
          src="./assets/[image-name].png"
          alt="[Descriptive alt text]"
          class="screenshot-panel__img"
          loading="lazy"
        />
      </div>
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
    <span data-lang="pt">[Mensagem de aviso]</span>
  </div>
</div>

<!-- Info -->
<div class="callout callout--info">
  <span class="callout__icon">ℹ️</span>
  <div class="callout__body">
    <span data-lang="en">[Info message]</span>
    <span data-lang="pt">[Mensagem informativa]</span>
  </div>
</div>

<!-- Conditional Step -->
<div class="callout callout--conditional">
  <span class="callout__icon">🔀</span>
  <div class="callout__body">
    <span data-lang="en">[Conditional note]</span>
    <span data-lang="pt">[Nota condicional]</span>
  </div>
</div>
```

## JavaScript Requirements

Include these interactions:

```javascript
// Progress bar
window.addEventListener('scroll', () => {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = (scrollTop / docHeight) * 100;
  document.getElementById('progressFill').style.width = `${progress}%`;
});

// Sidebar toggle (tablet/mobile)
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.getElementById('sidebar');
const sidebarOverlay = document.getElementById('sidebarOverlay');
const sidebarClose = document.getElementById('sidebarClose');

function toggleSidebar() {
  menuToggle.classList.toggle('open');
  sidebar.classList.toggle('open');
  sidebarOverlay.classList.toggle('active');
}

menuToggle.addEventListener('click', toggleSidebar);
sidebarOverlay.addEventListener('click', toggleSidebar);
sidebarClose.addEventListener('click', toggleSidebar);

// Close sidebar when clicking a link (mobile)
sidebar.querySelectorAll('.sidebar__link').forEach(link => {
  link.addEventListener('click', () => {
    if (window.innerWidth < 1200) {
      toggleSidebar();
    }
  });
});

// Language switching
document.getElementById('langSelect').addEventListener('change', (e) => {
  document.body.setAttribute('data-lang', e.target.value);
});
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
- Reference images when helpful

### Sidebar Descriptions
- Keep to 1-2 lines
- Use patterns like:
  - "5 sub-steps"
  - "Conditional step"
  - "Final step"
  - "Quick verification"

### Images
- Place in `image-container` for full-width display
- Use `screenshot-panel` for side-by-side layout
- Images are NOT clickable (no zoom)
- Center images in containers
- Use light tinted background

## Section Breakdown Example

For a 7-step installation guide:

| Step | Title | Sidebar Description | Focus |
|------|-------|---------------------|-------|
| 1 | Unboxing | 5 sub-steps | Physical setup, power, connection |
| 2 | Provisioning | 1 sub-step | Device configuration state |
| 3 | Check Network | 3 sub-steps | Connectivity verification |
| 4 | Diagnostics | 1 sub-step | Health check |
| 5 | General Settings | 5 sub-steps | Configuration options |
| 6 | Mounting | 8 sub-steps | Physical installation |
| 7 | External Camera | Conditional step | Optional external camera |
| 8 | Complete Installation | Final step | Final verification |
