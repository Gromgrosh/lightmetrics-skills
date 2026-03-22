# Product Specification Template

Use this template for technical specifications, feature documentation, and product requirement documents.

## Document Structure

```
1. Title & Overview
   - Product name and version
   - Executive summary
   - Key features list
   - Target audience

2. Technical Specifications
   - Hardware requirements
   - Software requirements
   - Compatibility matrix
   - Performance metrics

3. Feature Documentation
   - Feature name
   - Description
   - Use cases
   - Configuration options
   - Screenshots/diagrams

4. Integration Guide
   - API endpoints (if applicable)
   - Data formats
   - Authentication
   - Examples

5. Appendices
   - Glossary
   - Version history
   - References
```

## HTML Structure Pattern

### Product Header
```html
<div class="spec-header">
  <div class="spec-header__badge">v2.0</div>
  <h1 class="spec-header__title">
    <span data-lang="en">[Product Name]</span>
    <span data-lang="pt">[Portuguese Name]</span>
  </h1>
  <p class="spec-header__subtitle">
    <span data-lang="en">Technical Specification</span>
    <span data-lang="pt">Especificação Técnica</span>
  </p>
</div>
```

### Specification Table
```html
<section class="spec-section" id="hardware">
  <h2 class="spec-section__title">
    <span data-lang="en">Hardware Requirements</span>
    <span data-lang="pt">Requisitos de Hardware</span>
  </h2>
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
    </tbody>
  </table>
</section>
```

### Feature Card
```html
<div class="feature-card">
  <div class="feature-card__header">
    <span class="feature-card__icon">🔧</span>
    <h3 class="feature-card__title">
      <span data-lang="en">[Feature Name]</span>
      <span data-lang="pt">[Portuguese Name]</span>
    </h3>
  </div>
  <p class="feature-card__desc">
    <span data-lang="en">[Feature description]</span>
    <span data-lang="pt">[Portuguese description]</span>
  </p>
  <ul class="feature-card__list">
    <li><span data-lang="en">[Capability 1]</span><span data-lang="pt">[Portuguese]</span></li>
    <li><span data-lang="en">[Capability 2]</span><span data-lang="pt">[Portuguese]</span></li>
  </ul>
</div>
```

### Compatibility Matrix
```html
<div class="compat-matrix">
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
- Provide visual examples where helpful

### Versioning
- Clearly mark version-specific features
- Use badges or tags for deprecations
- Include "Added in vX.X" notes
