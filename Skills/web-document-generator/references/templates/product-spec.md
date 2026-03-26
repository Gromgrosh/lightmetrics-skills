# Product Specification Template

Use this template for technical specifications, feature documentation, and product requirement documents.

> **Note**: This template follows the [Common Template Specification](./common-template-spec.md) for header, sidebar, hero, and image handling.

## Document Structure

```
1. Header (from common spec)
   - Logo + document name + platform
   - Language selector
   - Hamburger menu (tablet/mobile)
   - Progress bar

2. Side Panel (from common spec)
   - Section title ("SPECIFICATIONS" or similar)
   - Numbered items with descriptions
   - Back to top link
   - Document date

3. Hero Section
   - Product/Platform eyebrow
   - Specification title
   - Description paragraph

4. Specification Sections
   - Section badge + title
   - Description
   - Specification tables
   - Feature cards
   - Images in tinted containers

5. Appendices
   - Glossary
   - Version history
   - References
```

## HTML Structure Pattern

### Complete Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Product Name] — Technical Specification</title>
  <link rel="stylesheet" href="./styles.css">
</head>
<body data-lang="en">

  <!-- Header -->
  <header class="site-header">
    <a href="#" class="site-header__brand">
      <img src="./assets/lightmetrics-logo.svg" alt="Lightmetrics" class="brand-logo-img" />
      <span class="brand-divider"></span>
      <span class="brand-text">
        <span class="brand-name">Technical Specification</span>
        <span class="brand-sub">[Product Name]</span>
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
      <span>SPECIFICATIONS</span>
      <button class="sidebar__close" id="sidebarClose" aria-label="Close menu">✕</button>
    </div>

    <ul class="sidebar__list">
      <li>
        <a href="#overview" class="sidebar__link">
          <span class="sidebar__num">1</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Overview</span>
            <span class="sidebar__subtitle">Product summary</span>
          </span>
        </a>
      </li>
      <li>
        <a href="#hardware" class="sidebar__link">
          <span class="sidebar__num">2</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Hardware</span>
            <span class="sidebar__subtitle">Requirements & specs</span>
          </span>
        </a>
      </li>
      <!-- Repeat for each section -->
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
      <!-- Specification Sections -->
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
    <span data-lang="en">[PRODUCT NAME] v2.0</span>
    <span data-lang="pt">[NOME DO PRODUTO] v2.0</span>
  </p>
  <h1 class="page-hero__title">
    <span data-lang="en">Technical Specification</span>
    <span data-lang="pt">Especificação Técnica</span>
  </h1>
  <p class="page-hero__desc">
    <span data-lang="en">[Comprehensive technical specifications including hardware requirements, software compatibility, and feature documentation.]</span>
    <span data-lang="pt">[Especificações técnicas abrangentes]</span>
  </p>
</div>
```

### Specification Section

```html
<section class="step-section" id="hardware">
  <div class="step-section__header">
    <div class="step-section__meta">
      <span class="step-section__badge">
        <span data-lang="en">Section 1</span>
        <span data-lang="pt">Seção 1</span>
      </span>
    </div>
    <h2 class="step-section__title">
      <span data-lang="en">Hardware Requirements</span>
      <span data-lang="pt">Requisitos de Hardware</span>
    </h2>
    <p class="step-section__purpose">
      <span data-lang="en">[Section description and purpose]</span>
      <span data-lang="pt">[Descrição da seção]</span>
    </p>
  </div>

  <div class="step-section__substeps">
    <!-- Content blocks go here -->
  </div>
</section>
```

### Specification Table

```html
<div class="substep" id="hardware-specs">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">1.1</span>
      <h3 class="substep__title">
        <span data-lang="en">System Requirements</span>
        <span data-lang="pt">Requisitos do Sistema</span>
      </h3>
    </div>

    <table class="spec-table">
      <thead>
        <tr>
          <th><span data-lang="en">Component</span><span data-lang="pt">Componente</span></th>
          <th><span data-lang="en">Minimum</span><span data-lang="pt">Mínimo</span></th>
          <th><span data-lang="en">Recommended</span><span data-lang="pt">Recomendado</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Processor</td>
          <td>2.0 GHz dual-core</td>
          <td>3.0 GHz quad-core</td>
        </tr>
        <tr>
          <td>Memory</td>
          <td>4 GB RAM</td>
          <td>8 GB RAM</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

### Feature Card

```html
<div class="substep" id="feature-1">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">2.1</span>
      <h3 class="substep__title">
        <span data-lang="en">[Feature Name]</span>
        <span data-lang="pt">[Nome do Recurso]</span>
      </h3>
    </div>

    <p class="substep__desc">
      <span data-lang="en">[Feature description and user benefit]</span>
      <span data-lang="pt">[Descrição do recurso]</span>
    </p>

    <ul class="substep__instructions">
      <li>
        <span data-lang="en">[Capability 1]</span>
        <span data-lang="pt">[Capacidade 1]</span>
      </li>
      <li>
        <span data-lang="en">[Capability 2]</span>
        <span data-lang="pt">[Capacidade 2]</span>
      </li>
    </ul>

    <!-- Feature screenshot in tinted container -->
    <figure class="image-container">
      <img
        src="./assets/feature-screenshot.png"
        alt="[Feature name] interface showing [key elements]"
        loading="lazy"
      />
    </figure>
  </div>
</div>
```

### Compatibility Matrix

```html
<div class="substep" id="compatibility">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">3.0</span>
      <h3 class="substep__title">
        <span data-lang="en">Compatibility Matrix</span>
        <span data-lang="pt">Matriz de Compatibilidade</span>
      </h3>
    </div>

    <table class="compat-matrix__table">
      <thead>
        <tr>
          <th>Platform</th>
          <th>v1.0</th>
          <th>v2.0</th>
          <th>v3.0</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>iOS 14+</td>
          <td class="compat-matrix__yes">✓</td>
          <td class="compat-matrix__yes">✓</td>
          <td class="compat-matrix__yes">✓</td>
        </tr>
        <tr>
          <td>Android 10+</td>
          <td class="compat-matrix__no">✗</td>
          <td class="compat-matrix__yes">✓</td>
          <td class="compat-matrix__yes">✓</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

### Diagram/Image Block

```html
<div class="substep" id="architecture">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">4.0</span>
      <h3 class="substep__title">
        <span data-lang="en">System Architecture</span>
        <span data-lang="pt">Arquitetura do Sistema</span>
      </h3>
    </div>

    <p>
      <span data-lang="en">[Architecture description]</span>
      <span data-lang="pt">[Descrição da arquitetura]</span>
    </p>

    <!-- Architecture diagram in tinted container (NOT clickable) -->
    <figure class="image-container image-container--large">
      <img
        src="./assets/architecture-diagram.png"
        alt="System architecture showing [key components]"
        loading="lazy"
      />
    </figure>
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

### Technical Accuracy
- Use precise measurements and units
- Include version numbers for all software
- Specify exact model numbers for hardware
- Note any regional variations

### Specification Tables
- Group related specs logically
- Use consistent units throughout
- Include both minimum and recommended values
- Note any conditional requirements

### Feature Documentation
- Start with the user benefit
- Include concrete use cases
- Document all configuration options
- Provide visual examples in tinted containers

### Sidebar Descriptions
- Keep to 1-2 lines
- Use patterns like:
  - "Requirements & specs"
  - "3 features"
  - "Compatibility info"
  - "API reference"

### Images
- Place in `image-container` for diagrams and screenshots
- Images are NOT clickable (no zoom)
- Center images in containers with light tinted background
- Use descriptive alt text

## Section Breakdown Example

| Section | Title | Sidebar Description | Focus |
|---------|-------|---------------------|-------|
| 1 | Overview | Product summary | Executive summary, key features |
| 2 | Hardware | Requirements & specs | System requirements, compatibility |
| 3 | Software | Dependencies | OS, frameworks, versions |
| 4 | Features | 5 features | Feature documentation with screenshots |
| 5 | Integration | API reference | Endpoints, examples |
| 6 | Appendix | Reference tables | Error codes, glossary |
