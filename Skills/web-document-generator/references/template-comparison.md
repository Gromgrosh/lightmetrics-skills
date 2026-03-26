# Template Type Structural Impact — Web Document Generator

## Overview

The web-document-generator skill has **4 template types**, each with distinct structural patterns optimized for different documentation purposes.

---

## Quick Comparison

| Aspect | Installation Guide | Product Spec | Process Workflow | Technical Manual |
|--------|-------------------|--------------|-----------------|-----------------|
| **Primary Structure** | Sequential numbered steps | Categorical tables | Numbered workflow stages | Chapters with procedures |
| **Visual Focus** | Screenshots + instructions | Data tables + matrices | Decision points + roles | Code blocks + procedures |
| **Branching Logic** | Decision tables, conditionals | N/A | Decision diamonds, exceptions | Error codes, alternatives |
| **Metadata** | Prerequisites, time estimate | Version, specs | Owner, updated date | Last updated, index |
| **Role Focus** | End users, installers | Technical decision-makers | Process actors/roles | System admins, developers |
| **Content Density** | Moderate (step-by-step) | High (reference data) | Moderate (process-focused) | Very high (comprehensive) |

---

## Document Structure Comparison

### Installation Guide
```
1. Title & Overview
   - Document title, purpose, audience
   - Time estimate (optional)
   - Prerequisites chip list

2. Steps Section (repeat for each major step)
   - Step number/title + indicator (STEP 01/07)
   - Purpose statement
   - Sub-steps (numbered 1.1, 1.2...)
     - Action + Screenshot
     - Decision points table
   - Completion criteria

3. General Reference (optional)
   - Common dialogs, troubleshooting, glossary

4. Footer
   - Version, last updated, contact
```

### Product Specification
```
1. Title & Overview
   - Product name + version badge
   - Executive summary
   - Key features list

2. Technical Specifications
   - Hardware requirements (min/recommended)
   - Software requirements
   - Compatibility matrix
   - Performance metrics

3. Feature Documentation
   - Feature cards with icon, description, capabilities

4. Integration Guide (if applicable)
   - API endpoints, data formats, examples

5. Appendices
   - Glossary, version history
```

### Process Workflow
```
1. Process Overview
   - Process name, purpose, scope
   - RACI matrix (optional)

2. Prerequisites
   - Permissions, system access, dependencies

3. Process Flow
   - Stage cards with:
     - Stage name + number
     - Actor/Role
     - Actions list
     - Input/Output blocks
     - Decision points

4. Exception Handling
   - Exception cards with trigger/resolution/escalation

5. Reference Materials
   - Related processes, contacts
```

### Technical Manual
```
1. Front Matter
   - Title, TOC, conventions

2. Introduction
   - System overview, architecture, terminology

3. Getting Started
   - Prerequisites, installation, quick start

4. Core Functionality
   - Chapters with:
     - Chapter number/title
     - Introduction
     - Procedure blocks (time, prereqs, steps, result)
     - Code blocks
     - Configuration tables

5. Administration
   - User management, maintenance, backup

6. API Reference (if applicable)
   - Endpoints with method, path, params, examples

7. Appendices
   - Error codes, glossary, index
```

---

## HTML Components by Template

### Installation Guide Components

| Component | CSS Class | Purpose |
|-----------|-----------|---------|
| Hero | `.page-hero` | Product name, title, description, prerequisite chips |
| Step Section | `.step-section` | Major step with badge (STEP 01/07), title, purpose |
| Sub-step | `.substep` | Numbered sub-step with dual-column (text + screenshot) |
| Screenshot Panel | `.screenshot-panel` | Image with caption, lazy-loaded |
| Decision Table | `.decision-table` | Collapsible `<details>` with situation/action pairs |
| Callout | `.callout--warning/info/conditional` | Alert boxes with emoji icon |

**Unique Features:**
- Step progression indicator (STEP 01/07)
- Screenshot integration in every sub-step
- Collapsible decision branching

---

### Product Specification Components

| Component | CSS Class | Purpose |
|-----------|-----------|---------|
| Header | `.spec-header` | Version badge, product name, subtitle |
| Section | `.spec-section` | Major category (Hardware, Software, etc.) |
| Spec Table | `.spec-table` | Component/Minimum/Recommended columns |
| Feature Card | `.feature-card` | Icon, title, description, capability list |
| Compat Matrix | `.compat-matrix` | Platform × Version grid with ✓/✗ |

**Unique Features:**
- Min/Recommended columns in tables
- Feature cards with icon headers
- Compatibility matrices with semantic styling

---

### Process Workflow Components

| Component | CSS Class | Purpose |
|-----------|-----------|---------|
| Header | `.process-header` | Category, title, owner, updated date |
| Stage Card | `.stage-card` | Numbered stage with actor, actions, I/O |
| Decision Point | `.decision-point` | Diamond icon with yes/no path branches |
| RACI Matrix | `.raci-matrix` | Responsibility assignment with R/A/C/I legend |
| Exception Card | `.exception-card` | Trigger, resolution steps, escalation path |

**Unique Features:**
- Actor/Role designation per stage
- Input/Output documentation blocks
- Decision diamonds with branching paths
- Exception handling with escalation

---

### Technical Manual Components

| Component | CSS Class | Purpose |
|-----------|-----------|---------|
| TOC | `.manual-toc` | Hierarchical navigation with chapter/section links |
| Chapter | `.manual-chapter` | Numbered chapter with title, intro paragraph |
| Procedure | `.procedure` | Named procedure with time, prereqs, steps, result |
| Code Block | `.code-block` | Syntax-highlighted code with language badge, copy button |
| Config Table | `.config-table` | Parameter/Type/Default/Description columns |
| API Endpoint | `.api-endpoint` | Method badge (GET/POST), path, params, example response |
| Error Codes | `.error-codes` | Code/Message/Resolution table |

**Unique Features:**
- Full table of contents with anchors
- Procedure blocks with time estimates
- Code blocks with copy functionality
- API endpoint documentation
- Error code reference tables

---

## Hierarchy Depth Comparison

| Template | Levels | Hierarchy Pattern |
|----------|--------|-------------------|
| Installation Guide | 3 | Document → Step → Sub-step |
| Product Spec | 3 | Document → Section → Item (table row/card) |
| Process Workflow | 4 | Document → Stage → Action → Decision/Exception |
| Technical Manual | 5 | Document → Chapter → Section → Procedure → Step |

---

## Signature HTML Patterns

### Installation Guide — Step with Sub-step
```html
<!-- Major step container - each step gets its own section with unique ID for navigation -->
<section class="step-section" id="step-1">

  <!-- Step header: displays step number badge, title, and progress indicator -->
  <div class="step-section__header">
    <span class="step-section__badge">Step 1</span>          <!-- Styled pill/badge -->
    <h2 class="step-section__title">[Title]</h2>             <!-- Main step heading -->
    <p class="step-section__indicator">STEP 01/07</p>        <!-- Progress: current/total -->
  </div>

  <!-- Sub-step: granular instruction within the major step -->
  <div class="substep" id="step-1-1">
    <!-- Inner wrapper: --with-screenshot modifier enables two-column layout -->
    <div class="substep__inner substep__inner--with-screenshot">

      <!-- Left column: text instructions -->
      <div class="substep__content">
        <span class="substep__badge">1.1</span>              <!-- Sub-step number -->
        <ol class="substep__instructions">...</ol>           <!-- Numbered action list -->
      </div>

      <!-- Right column: visual reference -->
      <div class="screenshot-panel">
        <img src="..." loading="lazy" />                     <!-- Lazy-loaded screenshot -->
      </div>

    </div>
  </div>

</section>
```

### Product Spec — Feature Card
```html
<!-- Feature card: self-contained block showcasing a single product feature -->
<div class="feature-card">

  <!-- Header row: icon + title for quick scanning -->
  <div class="feature-card__header">
    <span class="feature-card__icon">🔧</span>               <!-- Visual identifier (emoji or SVG) -->
    <h3 class="feature-card__title">[Feature Name]</h3>      <!-- Feature name as heading -->
  </div>

  <!-- Brief explanation of what this feature does -->
  <p class="feature-card__desc">[Description]</p>

  <!-- Bulleted list of specific capabilities this feature provides -->
  <ul class="feature-card__list">
    <li>[Capability 1]</li>                                  <!-- Individual capability -->
    <li>[Capability 2]</li>                                  <!-- Add more as needed -->
  </ul>

</div>
```

### Process Workflow — Decision Point
```html
<!-- Decision point: represents a branching moment in the workflow -->
<div class="decision-point">

  <!-- Visual diamond shape (styled via CSS) - classic flowchart symbol -->
  <div class="decision-point__diamond">?</div>

  <!-- Decision content: question and possible paths -->
  <div class="decision-point__content">

    <!-- The yes/no question that determines the branch -->
    <h4 class="decision-point__question">[Question?]</h4>

    <!-- Container for the two possible outcomes -->
    <div class="decision-point__paths">

      <!-- "Yes" branch: what happens if condition is true -->
      <div class="decision-point__path decision-point__path--yes">
        <span class="decision-point__label">Yes</span>       <!-- Branch label -->
        → [Action if yes]                                    <!-- Next step or outcome -->
      </div>

      <!-- "No" branch: what happens if condition is false -->
      <div class="decision-point__path decision-point__path--no">
        <span class="decision-point__label">No</span>        <!-- Branch label -->
        → [Action if no]                                     <!-- Alternative step -->
      </div>

    </div>
  </div>

</div>
```

### Technical Manual — Procedure Block
```html
<!-- Procedure block: self-contained task with all context needed to complete it -->
<div class="procedure" id="procedure-name">

  <!-- Header: procedure title + estimated duration -->
  <div class="procedure__header">
    <h4 class="procedure__title">[Procedure Name]</h4>       <!-- What this procedure accomplishes -->
    <span class="procedure__time">~5 min</span>              <!-- Time estimate badge -->
  </div>

  <!-- Prerequisites: what must be true before starting -->
  <div class="procedure__prereq">
    <strong>Before you begin:</strong>
    <ul><li>[Prerequisite]</li></ul>                         <!-- Required conditions/access/tools -->
  </div>

  <!-- Step-by-step instructions (numbered list) -->
  <ol class="procedure__steps">
    <li class="procedure__step">[Step instruction]</li>      <!-- Individual action to perform -->
  </ol>

  <!-- Expected outcome: how to verify success -->
  <div class="procedure__result">
    <strong>Result:</strong> [Expected outcome]              <!-- What user should see/have after -->
  </div>

</div>
```

---

## Template Source Files

Located in: `projects/Lightmetrics/web-document-generator/references/templates/`

| Template | File | Lines |
|----------|------|-------|
| Installation Guide | `installation-guide.md` | 216 |
| Product Specification | `product-spec.md` | 157 |
| Process Workflow | `process-workflow.md` | 217 |
| Technical Manual | `technical-manual.md` | 269 |

---

## Common Elements Across All Templates

All templates share:
- **Light Spectrum design tokens** — Plum primary (#8B2682), Eastern Blue secondary (#2898A2)
- **Fluid typography** — CSS `clamp()` for responsive sizing
- **Multi-language support** — `data-lang="en"` / `data-lang="pt"` attributes
- **Responsive breakpoints** — Mobile (<640px), Tablet (640-1023px), Desktop (1024-1199px), Large (≥1200px)
- **Print styles** — Optimized for PDF export
- **BEM naming** — Block__Element--Modifier pattern for all CSS classes
