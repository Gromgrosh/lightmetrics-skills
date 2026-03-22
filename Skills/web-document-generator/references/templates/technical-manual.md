# Technical Manual Template

Use this template for comprehensive reference documentation, system administration guides, and detailed technical references.

## Document Structure

```
1. Front Matter
   - Title page
   - Table of contents
   - About this document
   - Conventions used

2. Introduction
   - System overview
   - Architecture diagram
   - Key concepts
   - Terminology

3. Getting Started
   - Prerequisites
   - Installation
   - Initial configuration
   - Quick start guide

4. Core Functionality
   - Feature sections (repeat)
     - Overview
     - Detailed procedures
     - Configuration options
     - Examples
     - Troubleshooting

5. Administration
   - User management
   - System configuration
   - Maintenance procedures
   - Backup and recovery

6. API Reference (if applicable)
   - Endpoints
   - Parameters
   - Response formats
   - Examples

7. Appendices
   - Error codes
   - Glossary
   - Index
   - Version history
```

## HTML Structure Pattern

### Table of Contents
```html
<nav class="manual-toc">
  <h2 class="manual-toc__title">
    <span data-lang="en">Contents</span>
    <span data-lang="pt">Conteúdo</span>
  </h2>
  <ol class="manual-toc__list">
    <li class="manual-toc__chapter">
      <a href="#chapter-1" class="manual-toc__link">
        <span class="manual-toc__number">1</span>
        <span class="manual-toc__text">
          <span data-lang="en">[Chapter Title]</span>
          <span data-lang="pt">[Portuguese Title]</span>
        </span>
      </a>
      <ol class="manual-toc__sections">
        <li><a href="#section-1-1">1.1 [Section]</a></li>
        <li><a href="#section-1-2">1.2 [Section]</a></li>
      </ol>
    </li>
  </ol>
</nav>
```

### Chapter Section
```html
<section class="manual-chapter" id="chapter-1">
  <div class="manual-chapter__header">
    <span class="manual-chapter__number">Chapter 1</span>
    <h2 class="manual-chapter__title">
      <span data-lang="en">[Chapter Title]</span>
      <span data-lang="pt">[Portuguese Title]</span>
    </h2>
  </div>

  <div class="manual-chapter__intro">
    <p>
      <span data-lang="en">[Introduction paragraph]</span>
      <span data-lang="pt">[Portuguese paragraph]</span>
    </p>
  </div>

  <!-- Sections go here -->
</section>
```

### Procedure Block
```html
<div class="procedure" id="procedure-name">
  <div class="procedure__header">
    <h4 class="procedure__title">
      <span data-lang="en">[Procedure Name]</span>
      <span data-lang="pt">[Portuguese Name]</span>
    </h4>
    <span class="procedure__time">~5 min</span>
  </div>

  <div class="procedure__prereq">
    <strong><span data-lang="en">Before you begin:</span><span data-lang="pt">Antes de começar:</span></strong>
    <ul>
      <li><span data-lang="en">[Prerequisite 1]</span><span data-lang="pt">[Portuguese]</span></li>
    </ul>
  </div>

  <ol class="procedure__steps">
    <li class="procedure__step">
      <div class="procedure__step-content">
        <span data-lang="en">[Step instruction]</span>
        <span data-lang="pt">[Portuguese instruction]</span>
      </div>
      <div class="procedure__step-note">
        <span data-lang="en">[Additional note]</span>
        <span data-lang="pt">[Portuguese note]</span>
      </div>
    </li>
  </ol>

  <div class="procedure__result">
    <strong><span data-lang="en">Result:</span><span data-lang="pt">Resultado:</span></strong>
    <span data-lang="en">[Expected outcome]</span>
    <span data-lang="pt">[Portuguese outcome]</span>
  </div>
</div>
```

### Code Block
```html
<div class="code-block">
  <div class="code-block__header">
    <span class="code-block__lang">bash</span>
    <button class="code-block__copy" onclick="copyCode(this)">Copy</button>
  </div>
  <pre class="code-block__pre"><code class="code-block__code">npm install @lightmetrics/sdk
./configure --enable-logging
make install</code></pre>
</div>
```

### Configuration Table
```html
<div class="config-table">
  <h4 class="config-table__title">
    <span data-lang="en">Configuration Options</span>
    <span data-lang="pt">Opções de Configuração</span>
  </h4>
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
        <td><span data-lang="en">Connection timeout in seconds</span><span data-lang="pt">Tempo limite de conexão em segundos</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

### API Endpoint
```html
<div class="api-endpoint">
  <div class="api-endpoint__header">
    <span class="api-endpoint__method api-endpoint__method--get">GET</span>
    <code class="api-endpoint__path">/api/v1/devices/{id}</code>
  </div>

  <div class="api-endpoint__desc">
    <span data-lang="en">[Endpoint description]</span>
    <span data-lang="pt">[Portuguese description]</span>
  </div>

  <div class="api-endpoint__params">
    <h5><span data-lang="en">Parameters</span><span data-lang="pt">Parâmetros</span></h5>
    <table>
      <tr>
        <td><code>id</code></td>
        <td>string</td>
        <td>required</td>
        <td><span data-lang="en">Device identifier</span><span data-lang="pt">Identificador do dispositivo</span></td>
      </tr>
    </table>
  </div>

  <div class="api-endpoint__example">
    <h5><span data-lang="en">Example Response</span><span data-lang="pt">Exemplo de Resposta</span></h5>
    <pre><code>{
  "id": "dev_123",
  "status": "online",
  "lastSeen": "2024-01-15T10:30:00Z"
}</code></pre>
  </div>
</div>
```

### Error Code Table
```html
<div class="error-codes">
  <h3 class="error-codes__title">
    <span data-lang="en">Error Codes</span>
    <span data-lang="pt">Códigos de Erro</span>
  </h3>
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
        <td><span data-lang="en">Check network connectivity</span><span data-lang="pt">Verifique a conectividade de rede</span></td>
      </tr>
    </tbody>
  </table>
</div>
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

### Navigation
- Use clear heading hierarchy
- Include anchor links for all sections
- Provide "See also" references
- Include searchable index terms

### Maintenance
- Include last-updated timestamps
- Mark deprecated features clearly
- Note planned changes
- Provide feedback channels
