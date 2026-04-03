# Process Workflow Template

Use this template for business process documentation, operational workflows, and procedural guides.

> **Note**: This template follows the [Common Template Specification](./common-template-spec.md) for header, sidebar, hero, and image handling.

## Document Structure

```
1. Header (from common spec)
   - Logo + document name + platform
   - Language selector
   - Hamburger menu (tablet/mobile)
   - Progress bar

2. Side Panel (from common spec)
   - Section title ("PROCESS STAGES" or similar)
   - Numbered stages with descriptions
   - Back to top link
   - Document date

3. Hero Section
   - Category/Department eyebrow
   - Process title
   - Purpose description

4. Process Stages
   - Stage badge + title
   - Actor/Role
   - Actions list
   - Inputs/Outputs
   - Decision points
   - Diagrams in tinted containers

5. Exception Handling
   - Common exceptions
   - Escalation paths
   - Recovery procedures

6. Reference Materials
   - Related processes
   - RACI matrix
   - Contact information
```

## HTML Structure Pattern

### Complete Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Process Name] — Workflow Guide</title>
  <link rel="stylesheet" href="./styles.css">
</head>
<body data-lang="en">

  <!-- Header -->
  <header class="site-header">
    <a href="#" class="site-header__brand">
      <img src="./assets/brand/brand_lightmetrics-logo.webp" alt="Lightmetrics" class="brand-logo-img" />
      <span class="brand-divider"></span>
      <span class="brand-text">
        <span class="brand-name">Workflow Guide</span>
        <span class="brand-sub">[Department/Category]</span>
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
      <span>PROCESS STAGES</span>
      <button class="sidebar__close" id="sidebarClose" aria-label="Close menu">✕</button>
    </div>

    <ul class="sidebar__list">
      <li>
        <a href="#stage-1" class="sidebar__link">
          <span class="sidebar__num">1</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Initiation</span>
            <span class="sidebar__subtitle">Request submission</span>
          </span>
        </a>
      </li>
      <li>
        <a href="#stage-2" class="sidebar__link">
          <span class="sidebar__num">2</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Review</span>
            <span class="sidebar__subtitle">Manager approval</span>
          </span>
        </a>
      </li>
      <!-- Repeat for each stage -->
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
      <!-- Process Stages -->
      <!-- Exception Handling -->
      <!-- Reference Materials -->
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
    <span data-lang="en">[DEPARTMENT / CATEGORY]</span>
    <span data-lang="pt">[DEPARTAMENTO / CATEGORIA]</span>
  </p>
  <h1 class="page-hero__title">
    <span data-lang="en">[Process Name]</span>
    <span data-lang="pt">[Nome do Processo]</span>
  </h1>
  <p class="page-hero__desc">
    <span data-lang="en">[Purpose statement explaining what this process accomplishes and who should follow it.]</span>
    <span data-lang="pt">[Declaração de propósito]</span>
  </p>
</div>
```

### Process Stage Section

```html
<section class="step-section" id="stage-1">
  <div class="step-section__header">
    <div class="step-section__meta">
      <span class="step-section__badge">
        <span data-lang="en">Stage 1</span>
        <span data-lang="pt">Etapa 1</span>
      </span>
    </div>
    <h2 class="step-section__title">
      <span data-lang="en">[Stage Name]</span>
      <span data-lang="pt">[Nome da Etapa]</span>
    </h2>
    <p class="step-section__indicator">
      <span data-lang="en">Actor: [Role Name]</span>
      <span data-lang="pt">Ator: [Nome do Papel]</span>
    </p>
    <p class="step-section__purpose">
      <span data-lang="en">[Stage purpose and expected outcome]</span>
      <span data-lang="pt">[Propósito da etapa]</span>
    </p>
  </div>

  <div class="step-section__substeps">
    <!-- Stage content blocks go here -->
  </div>
</section>
```

### Actions Block

```html
<div class="substep" id="stage-1-actions">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">1.0</span>
      <h3 class="substep__title">
        <span data-lang="en">Actions</span>
        <span data-lang="pt">Ações</span>
      </h3>
    </div>

    <ol class="substep__instructions">
      <li>
        <span data-lang="en">[Action 1 with specific details]</span>
        <span data-lang="pt">[Ação 1]</span>
      </li>
      <li>
        <span data-lang="en">[Action 2 with specific details]</span>
        <span data-lang="pt">[Ação 2]</span>
      </li>
      <li>
        <span data-lang="en">[Action 3 with specific details]</span>
        <span data-lang="pt">[Ação 3]</span>
      </li>
    </ol>

    <!-- Process diagram in tinted container (NOT clickable) -->
    <figure class="image-container">
      <img
        src="./assets/process-diagram.png"
        alt="Process flow showing [key stages]"
        loading="lazy"
      />
    </figure>
  </div>
</div>
```

### Input/Output Block

```html
<div class="substep" id="stage-1-io">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">1.1</span>
      <h3 class="substep__title">
        <span data-lang="en">Inputs & Outputs</span>
        <span data-lang="pt">Entradas e Saídas</span>
      </h3>
    </div>

    <div class="io-block">
      <div class="io-block__input">
        <strong><span data-lang="en">Input:</span><span data-lang="pt">Entrada:</span></strong>
        <ul>
          <li><span data-lang="en">[Input item 1]</span><span data-lang="pt">[Item 1]</span></li>
          <li><span data-lang="en">[Input item 2]</span><span data-lang="pt">[Item 2]</span></li>
        </ul>
      </div>
      <div class="io-block__output">
        <strong><span data-lang="en">Output:</span><span data-lang="pt">Saída:</span></strong>
        <ul>
          <li><span data-lang="en">[Output item 1]</span><span data-lang="pt">[Item 1]</span></li>
          <li><span data-lang="en">[Output item 2]</span><span data-lang="pt">[Item 2]</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

### Decision Point

```html
<div class="substep" id="stage-2-decision">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">2.0</span>
      <h3 class="substep__title">
        <span data-lang="en">Decision Point</span>
        <span data-lang="pt">Ponto de Decisão</span>
      </h3>
    </div>

    <div class="decision-point">
      <div class="decision-point__question">
        <strong><span data-lang="en">Question:</span><span data-lang="pt">Pergunta:</span></strong>
        <span data-lang="en">[Decision question to be answered]</span>
        <span data-lang="pt">[Pergunta de decisão]</span>
      </div>

      <div class="decision-point__paths">
        <div class="decision-point__path decision-point__path--yes">
          <span class="decision-point__label">
            <span data-lang="en">Yes</span>
            <span data-lang="pt">Sim</span>
          </span>
          <span data-lang="en">→ [Proceed to Stage 3]</span>
          <span data-lang="pt">→ [Prosseguir para Etapa 3]</span>
        </div>
        <div class="decision-point__path decision-point__path--no">
          <span class="decision-point__label">
            <span data-lang="en">No</span>
            <span data-lang="pt">Não</span>
          </span>
          <span data-lang="en">→ [Return to Stage 1 for revision]</span>
          <span data-lang="pt">→ [Retornar à Etapa 1 para revisão]</span>
        </div>
      </div>
    </div>

    <!-- Decision flowchart in tinted container -->
    <figure class="image-container">
      <img
        src="./assets/decision-flowchart.png"
        alt="Decision flowchart showing approval paths"
        loading="lazy"
      />
    </figure>
  </div>
</div>
```

### RACI Matrix

```html
<div class="substep" id="raci">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">R</span>
      <h3 class="substep__title">
        <span data-lang="en">Responsibility Matrix</span>
        <span data-lang="pt">Matriz de Responsabilidade</span>
      </h3>
    </div>

    <table class="raci-matrix__table">
      <thead>
        <tr>
          <th><span data-lang="en">Activity</span><span data-lang="pt">Atividade</span></th>
          <th>Manager</th>
          <th>Technician</th>
          <th>Quality</th>
          <th>Admin</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span data-lang="en">[Activity 1]</span><span data-lang="pt">[Atividade 1]</span></td>
          <td class="raci-matrix__a">A</td>
          <td class="raci-matrix__r">R</td>
          <td class="raci-matrix__c">C</td>
          <td class="raci-matrix__i">I</td>
        </tr>
        <tr>
          <td><span data-lang="en">[Activity 2]</span><span data-lang="pt">[Atividade 2]</span></td>
          <td class="raci-matrix__r">R</td>
          <td class="raci-matrix__c">C</td>
          <td class="raci-matrix__a">A</td>
          <td class="raci-matrix__i">I</td>
        </tr>
      </tbody>
    </table>

    <div class="raci-matrix__legend">
      <span><strong>R</strong> = <span data-lang="en">Responsible</span><span data-lang="pt">Responsável</span></span>
      <span><strong>A</strong> = <span data-lang="en">Accountable</span><span data-lang="pt">Aprovador</span></span>
      <span><strong>C</strong> = <span data-lang="en">Consulted</span><span data-lang="pt">Consultado</span></span>
      <span><strong>I</strong> = <span data-lang="en">Informed</span><span data-lang="pt">Informado</span></span>
    </div>
  </div>
</div>
```

### Exception Card

```html
<div class="substep" id="exception-1">
  <div class="substep__inner">
    <div class="callout callout--warning">
      <span class="callout__icon">⚠️</span>
      <div class="callout__body">
        <strong><span data-lang="en">[Exception Name]</span><span data-lang="pt">[Nome da Exceção]</span></strong>
      </div>
    </div>

    <div class="exception-details">
      <div class="exception-details__trigger">
        <strong><span data-lang="en">Trigger:</span><span data-lang="pt">Gatilho:</span></strong>
        <span data-lang="en">[When this exception occurs]</span>
        <span data-lang="pt">[Quando esta exceção ocorre]</span>
      </div>

      <div class="exception-details__resolution">
        <strong><span data-lang="en">Resolution:</span><span data-lang="pt">Resolução:</span></strong>
        <ol>
          <li><span data-lang="en">[Resolution step 1]</span><span data-lang="pt">[Passo 1]</span></li>
          <li><span data-lang="en">[Resolution step 2]</span><span data-lang="pt">[Passo 2]</span></li>
        </ol>
      </div>

      <div class="exception-details__escalation">
        <strong><span data-lang="en">Escalate to:</span><span data-lang="pt">Escalar para:</span></strong>
        <span>[Role/Contact Information]</span>
      </div>
    </div>
  </div>
</div>
```

## JavaScript Requirements

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

### Process Clarity
- Define clear start and end points
- Identify all actors/roles involved
- Document all decision points
- Specify timing requirements where applicable

### Action Items
- Use imperative verbs: "Submit", "Review", "Approve"
- Be specific about systems/tools used
- Include required data/documents
- Note any dependencies

### Decision Points
- Frame as yes/no questions where possible
- Document all possible paths
- Include criteria for each decision
- Note who makes the decision

### Sidebar Descriptions
- Keep to 1-2 lines
- Use patterns like:
  - "Request submission"
  - "Manager approval"
  - "3 decision points"
  - "Final verification"

### Images
- Place flowcharts and diagrams in `image-container`
- Images are NOT clickable (no zoom)
- Center images in containers with light tinted background
- Use descriptive alt text for accessibility

### Exception Handling
- Anticipate common failure modes
- Provide clear recovery steps
- Define escalation criteria
- Include contact information

## Section Breakdown Example

| Stage | Title | Sidebar Description | Actor |
|-------|-------|---------------------|-------|
| 1 | Initiation | Request submission | Requester |
| 2 | Review | Manager approval | Manager |
| 3 | Processing | 4 actions | Operations |
| 4 | Quality Check | Verification step | QA Team |
| 5 | Completion | Final sign-off | Manager |
| - | Exceptions | 3 scenarios | Various |
| - | RACI Matrix | Responsibilities | - |
