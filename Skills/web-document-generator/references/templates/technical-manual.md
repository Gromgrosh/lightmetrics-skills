# Technical Manual Template

Use this template for comprehensive reference documentation, system administration guides, and detailed technical references.

> **Note**: This template follows the [Common Template Specification](./common-template-spec.md) for header, sidebar, hero, and image handling.

## Document Structure

```
1. Header (from common spec)
   - Logo + document name + platform
   - Language selector
   - Hamburger menu (tablet/mobile)
   - Progress bar

2. Side Panel (from common spec)
   - Section title ("CHAPTERS" or "CONTENTS")
   - Numbered chapters with descriptions
   - Back to top link
   - Document date

3. Hero Section
   - Product/System eyebrow
   - Manual title
   - Description paragraph

4. Chapters
   - Chapter badge + title
   - Introduction paragraph
   - Sections with:
     - Section badge + title
     - Procedures
     - Code blocks
     - Configuration tables
     - Diagrams in tinted containers

5. API Reference (if applicable)
   - Endpoints
   - Parameters
   - Response formats

6. Appendices
   - Error codes
   - Glossary
   - Index
```

## HTML Structure Pattern

### Complete Page Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[System Name] — Technical Manual</title>
  <link rel="stylesheet" href="./styles.css">
</head>
<body data-lang="en">

  <!-- Header -->
  <header class="site-header">
    <a href="#" class="site-header__brand">
      <img src="./assets/lightmetrics-logo.svg" alt="Lightmetrics" class="brand-logo-img" />
      <span class="brand-divider"></span>
      <span class="brand-text">
        <span class="brand-name">Technical Manual</span>
        <span class="brand-sub">[System/Product Name]</span>
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
      <span>CHAPTERS</span>
      <button class="sidebar__close" id="sidebarClose" aria-label="Close menu">✕</button>
    </div>

    <ul class="sidebar__list">
      <li>
        <a href="#chapter-1" class="sidebar__link">
          <span class="sidebar__num">1</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Introduction</span>
            <span class="sidebar__subtitle">System overview</span>
          </span>
        </a>
      </li>
      <li>
        <a href="#chapter-2" class="sidebar__link">
          <span class="sidebar__num">2</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Getting Started</span>
            <span class="sidebar__subtitle">Installation & setup</span>
          </span>
        </a>
      </li>
      <li>
        <a href="#chapter-3" class="sidebar__link">
          <span class="sidebar__num">3</span>
          <span class="sidebar__text">
            <span class="sidebar__step-title">Core Features</span>
            <span class="sidebar__subtitle">5 sections</span>
          </span>
        </a>
      </li>
      <!-- Repeat for each chapter -->
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
      <!-- Chapters -->
      <!-- API Reference -->
      <!-- Appendices -->
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
    <span data-lang="en">[SYSTEM NAME] v2.0</span>
    <span data-lang="pt">[NOME DO SISTEMA] v2.0</span>
  </p>
  <h1 class="page-hero__title">
    <span data-lang="en">Technical Manual</span>
    <span data-lang="pt">Manual Técnico</span>
  </h1>
  <p class="page-hero__desc">
    <span data-lang="en">[Comprehensive technical reference covering installation, configuration, administration, and troubleshooting.]</span>
    <span data-lang="pt">[Referência técnica abrangente]</span>
  </p>
</div>
```

### Chapter Section

```html
<section class="step-section" id="chapter-1">
  <div class="step-section__header">
    <div class="step-section__meta">
      <span class="step-section__badge">
        <span data-lang="en">Chapter 1</span>
        <span data-lang="pt">Capítulo 1</span>
      </span>
    </div>
    <h2 class="step-section__title">
      <span data-lang="en">[Chapter Title]</span>
      <span data-lang="pt">[Título do Capítulo]</span>
    </h2>
    <p class="step-section__purpose">
      <span data-lang="en">[Chapter introduction and scope]</span>
      <span data-lang="pt">[Introdução do capítulo]</span>
    </p>
  </div>

  <div class="step-section__substeps">
    <!-- Sections go here -->
  </div>
</section>
```

### Section with Content

```html
<div class="substep" id="section-1-1">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">1.1</span>
      <h3 class="substep__title">
        <span data-lang="en">[Section Title]</span>
        <span data-lang="pt">[Título da Seção]</span>
      </h3>
    </div>

    <p>
      <span data-lang="en">[Section content explaining the concept or feature]</span>
      <span data-lang="pt">[Conteúdo da seção]</span>
    </p>

    <!-- Architecture diagram in tinted container (NOT clickable) -->
    <figure class="image-container">
      <img
        src="./assets/architecture-diagram.png"
        alt="System architecture showing [key components]"
        loading="lazy"
      />
    </figure>

    <p>
      <span data-lang="en">[Additional explanation following the diagram]</span>
      <span data-lang="pt">[Explicação adicional]</span>
    </p>
  </div>
</div>
```

### Procedure Block

```html
<div class="substep" id="procedure-install">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">2.1</span>
      <h3 class="substep__title">
        <span data-lang="en">[Procedure Name]</span>
        <span data-lang="pt">[Nome do Procedimento]</span>
      </h3>
    </div>

    <div class="callout callout--info">
      <span class="callout__icon">ℹ️</span>
      <div class="callout__body">
        <strong><span data-lang="en">Before you begin:</span><span data-lang="pt">Antes de começar:</span></strong>
        <ul>
          <li><span data-lang="en">[Prerequisite 1]</span><span data-lang="pt">[Pré-requisito 1]</span></li>
          <li><span data-lang="en">[Prerequisite 2]</span><span data-lang="pt">[Pré-requisito 2]</span></li>
        </ul>
      </div>
    </div>

    <ol class="substep__instructions">
      <li>
        <span data-lang="en">[Step 1 instruction]</span>
        <span data-lang="pt">[Instrução do passo 1]</span>
      </li>
      <li>
        <span data-lang="en">[Step 2 instruction]</span>
        <span data-lang="pt">[Instrução do passo 2]</span>
      </li>
      <li>
        <span data-lang="en">[Step 3 instruction]</span>
        <span data-lang="pt">[Instrução do passo 3]</span>
      </li>
    </ol>

    <!-- Screenshot in tinted container -->
    <figure class="image-container">
      <img
        src="./assets/procedure-result.png"
        alt="Expected result after completing procedure"
        loading="lazy"
      />
    </figure>

    <div class="callout callout--success">
      <span class="callout__icon">✓</span>
      <div class="callout__body">
        <strong><span data-lang="en">Result:</span><span data-lang="pt">Resultado:</span></strong>
        <span data-lang="en">[Expected outcome description]</span>
        <span data-lang="pt">[Descrição do resultado esperado]</span>
      </div>
    </div>
  </div>
</div>
```

### Code Block

```html
<div class="substep" id="code-example">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">3.2</span>
      <h3 class="substep__title">
        <span data-lang="en">Code Example</span>
        <span data-lang="pt">Exemplo de Código</span>
      </h3>
    </div>

    <p>
      <span data-lang="en">[Explanation of what this code does]</span>
      <span data-lang="pt">[Explicação do código]</span>
    </p>

    <div class="code-block">
      <div class="code-block__header">
        <span class="code-block__lang">bash</span>
        <button class="code-block__copy" onclick="copyCode(this)">Copy</button>
      </div>
      <pre class="code-block__pre"><code class="code-block__code">npm install @lightmetrics/sdk
./configure --enable-logging
make install</code></pre>
    </div>

    <p>
      <span data-lang="en">[Additional notes about the code]</span>
      <span data-lang="pt">[Notas adicionais]</span>
    </p>
  </div>
</div>
```

### Configuration Table

```html
<div class="substep" id="config-options">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">4.1</span>
      <h3 class="substep__title">
        <span data-lang="en">Configuration Options</span>
        <span data-lang="pt">Opções de Configuração</span>
      </h3>
    </div>

    <table class="config-table__table">
      <thead>
        <tr>
          <th><span data-lang="en">Parameter</span><span data-lang="pt">Parâmetro</span></th>
          <th><span data-lang="en">Type</span><span data-lang="pt">Tipo</span></th>
          <th><span data-lang="en">Default</span><span data-lang="pt">Padrão</span></th>
          <th><span data-lang="en">Description</span><span data-lang="pt">Descrição</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>timeout</code></td>
          <td>integer</td>
          <td>30</td>
          <td><span data-lang="en">Connection timeout in seconds</span><span data-lang="pt">Tempo limite em segundos</span></td>
        </tr>
        <tr>
          <td><code>retries</code></td>
          <td>integer</td>
          <td>3</td>
          <td><span data-lang="en">Number of retry attempts</span><span data-lang="pt">Número de tentativas</span></td>
        </tr>
        <tr>
          <td><code>logLevel</code></td>
          <td>string</td>
          <td>"info"</td>
          <td><span data-lang="en">Logging verbosity level</span><span data-lang="pt">Nível de verbosidade</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

### API Endpoint

```html
<div class="substep" id="api-devices">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge api-badge api-badge--get">GET</span>
      <h3 class="substep__title">
        <code>/api/v1/devices/{id}</code>
      </h3>
    </div>

    <p>
      <span data-lang="en">[Endpoint description and use case]</span>
      <span data-lang="pt">[Descrição do endpoint]</span>
    </p>

    <h4><span data-lang="en">Parameters</span><span data-lang="pt">Parâmetros</span></h4>
    <table class="config-table__table">
      <thead>
        <tr>
          <th><span data-lang="en">Name</span><span data-lang="pt">Nome</span></th>
          <th><span data-lang="en">Type</span><span data-lang="pt">Tipo</span></th>
          <th><span data-lang="en">Required</span><span data-lang="pt">Obrigatório</span></th>
          <th><span data-lang="en">Description</span><span data-lang="pt">Descrição</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>id</code></td>
          <td>string</td>
          <td>Yes</td>
          <td><span data-lang="en">Device identifier</span><span data-lang="pt">Identificador do dispositivo</span></td>
        </tr>
      </tbody>
    </table>

    <h4><span data-lang="en">Example Response</span><span data-lang="pt">Exemplo de Resposta</span></h4>
    <div class="code-block">
      <div class="code-block__header">
        <span class="code-block__lang">json</span>
        <button class="code-block__copy" onclick="copyCode(this)">Copy</button>
      </div>
      <pre class="code-block__pre"><code class="code-block__code">{
  "id": "dev_123",
  "status": "online",
  "lastSeen": "2024-01-15T10:30:00Z"
}</code></pre>
    </div>
  </div>
</div>
```

### Error Codes Table

```html
<div class="substep" id="error-codes">
  <div class="substep__inner">
    <div class="substep__header">
      <span class="substep__badge">A.1</span>
      <h3 class="substep__title">
        <span data-lang="en">Error Codes</span>
        <span data-lang="pt">Códigos de Erro</span>
      </h3>
    </div>

    <table class="error-codes__table">
      <thead>
        <tr>
          <th><span data-lang="en">Code</span><span data-lang="pt">Código</span></th>
          <th><span data-lang="en">Message</span><span data-lang="pt">Mensagem</span></th>
          <th><span data-lang="en">Resolution</span><span data-lang="pt">Resolução</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>E001</code></td>
          <td><span data-lang="en">Connection timeout</span><span data-lang="pt">Tempo limite de conexão</span></td>
          <td><span data-lang="en">Check network connectivity and retry</span><span data-lang="pt">Verifique a conectividade</span></td>
        </tr>
        <tr>
          <td><code>E002</code></td>
          <td><span data-lang="en">Authentication failed</span><span data-lang="pt">Falha de autenticação</span></td>
          <td><span data-lang="en">Verify credentials and permissions</span><span data-lang="pt">Verifique as credenciais</span></td>
        </tr>
        <tr>
          <td><code>E003</code></td>
          <td><span data-lang="en">Resource not found</span><span data-lang="pt">Recurso não encontrado</span></td>
          <td><span data-lang="en">Confirm resource ID exists</span><span data-lang="pt">Confirme que o ID existe</span></td>
        </tr>
      </tbody>
    </table>
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

// Copy code functionality
function copyCode(button) {
  const codeBlock = button.closest('.code-block');
  const code = codeBlock.querySelector('code').textContent;
  navigator.clipboard.writeText(code).then(() => {
    button.textContent = 'Copied!';
    setTimeout(() => {
      button.textContent = 'Copy';
    }, 2000);
  });
}
```

## Content Guidelines

### Comprehensive Coverage
- Document all features and options
- Include both common and edge cases
- Provide multiple examples
- Cross-reference related sections

### Technical Precision
- Use exact terminology consistently
- Include version-specific information
- Document limitations and known issues
- Provide accurate code samples

### Sidebar Descriptions
- Keep to 1-2 lines
- Use patterns like:
  - "System overview"
  - "Installation & setup"
  - "5 sections"
  - "API reference"
  - "Error codes"

### Images
- Place diagrams and screenshots in `image-container`
- Images are NOT clickable (no zoom)
- Center images in containers with light tinted background
- Use descriptive alt text
- Instructions can come before or after images

### Navigation
- Use clear heading hierarchy
- Include anchor links for all sections
- Provide "See also" references
- Include searchable index terms

### Maintenance
- Include last-updated timestamps in sidebar footer
- Mark deprecated features clearly
- Note planned changes
- Provide feedback channels

## Section Breakdown Example

| Chapter | Title | Sidebar Description | Focus |
|---------|-------|---------------------|-------|
| 1 | Introduction | System overview | Architecture, concepts |
| 2 | Getting Started | Installation & setup | Prerequisites, installation |
| 3 | Core Features | 5 sections | Feature documentation |
| 4 | Configuration | Settings reference | All configuration options |
| 5 | Administration | Maintenance tasks | User management, backup |
| 6 | API Reference | Endpoints & examples | REST API documentation |
| A | Appendix | Error codes | Troubleshooting reference |
