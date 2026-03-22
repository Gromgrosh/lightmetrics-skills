# Process Workflow Template

Use this template for business process documentation, operational workflows, and procedural guides.

## Document Structure

```
1. Process Overview
   - Process name
   - Purpose statement
   - Scope (what's included/excluded)
   - Stakeholders (RACI matrix optional)

2. Prerequisites
   - Required permissions
   - System access
   - Prior training
   - Dependencies

3. Process Flow
   - Visual flowchart (optional)
   - Stage-by-stage breakdown
     - Stage name
     - Actor/Role
     - Actions
     - Inputs/Outputs
     - Decision points

4. Exception Handling
   - Common exceptions
   - Escalation paths
   - Recovery procedures

5. Reference Materials
   - Related processes
   - Supporting documents
   - Contact information
```

## HTML Structure Pattern

### Process Header
```html
<div class="process-header">
  <span class="process-header__category">Operations</span>
  <h1 class="process-header__title">
    <span data-lang="en">[Process Name]</span>
    <span data-lang="pt">[Portuguese Name]</span>
  </h1>
  <div class="process-header__meta">
    <span class="process-header__owner">Owner: [Name/Role]</span>
    <span class="process-header__updated">Updated: [Date]</span>
  </div>
</div>
```

### Stage Card
```html
<div class="stage-card" id="stage-1">
  <div class="stage-card__header">
    <span class="stage-card__number">1</span>
    <div class="stage-card__info">
      <h3 class="stage-card__title">
        <span data-lang="en">[Stage Name]</span>
        <span data-lang="pt">[Portuguese Name]</span>
      </h3>
      <span class="stage-card__actor">
        <span data-lang="en">Actor: [Role]</span>
        <span data-lang="pt">Ator: [Role]</span>
      </span>
    </div>
  </div>

  <div class="stage-card__body">
    <div class="stage-card__section">
      <h4 class="stage-card__section-title">
        <span data-lang="en">Actions</span>
        <span data-lang="pt">Ações</span>
      </h4>
      <ol class="stage-card__actions">
        <li><span data-lang="en">[Action 1]</span><span data-lang="pt">[Portuguese]</span></li>
        <li><span data-lang="en">[Action 2]</span><span data-lang="pt">[Portuguese]</span></li>
      </ol>
    </div>

    <div class="stage-card__io">
      <div class="stage-card__input">
        <strong><span data-lang="en">Input:</span><span data-lang="pt">Entrada:</span></strong>
        <span data-lang="en">[Input description]</span>
        <span data-lang="pt">[Portuguese description]</span>
      </div>
      <div class="stage-card__output">
        <strong><span data-lang="en">Output:</span><span data-lang="pt">Saída:</span></strong>
        <span data-lang="en">[Output description]</span>
        <span data-lang="pt">[Portuguese description]</span>
      </div>
    </div>
  </div>
</div>
```

### Decision Point
```html
<div class="decision-point">
  <div class="decision-point__diamond">?</div>
  <div class="decision-point__content">
    <h4 class="decision-point__question">
      <span data-lang="en">[Decision question]</span>
      <span data-lang="pt">[Portuguese question]</span>
    </h4>
    <div class="decision-point__paths">
      <div class="decision-point__path decision-point__path--yes">
        <span class="decision-point__label">Yes</span>
        <span data-lang="en">→ [Next action]</span>
        <span data-lang="pt">→ [Portuguese action]</span>
      </div>
      <div class="decision-point__path decision-point__path--no">
        <span class="decision-point__label">No</span>
        <span data-lang="en">→ [Alternative action]</span>
        <span data-lang="pt">→ [Portuguese action]</span>
      </div>
    </div>
  </div>
</div>
```

### RACI Matrix
```html
<div class="raci-matrix">
  <h3 class="raci-matrix__title">
    <span data-lang="en">Responsibility Matrix</span>
    <span data-lang="pt">Matriz de Responsabilidade</span>
  </h3>
  <table class="raci-matrix__table">
    <thead>
      <tr>
        <th><span data-lang="en">Activity</span><span data-lang="pt">Atividade</span></th>
        <th>Manager</th>
        <th>Technician</th>
        <th>Quality</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>[Activity name]</td>
        <td class="raci-matrix__r">R</td>
        <td class="raci-matrix__a">A</td>
        <td class="raci-matrix__c">C</td>
      </tr>
    </tbody>
  </table>
  <div class="raci-matrix__legend">
    <span><strong>R</strong> = Responsible</span>
    <span><strong>A</strong> = Accountable</span>
    <span><strong>C</strong> = Consulted</span>
    <span><strong>I</strong> = Informed</span>
  </div>
</div>
```

### Exception Card
```html
<div class="exception-card">
  <div class="exception-card__header">
    <span class="exception-card__icon">⚠️</span>
    <h4 class="exception-card__title">
      <span data-lang="en">[Exception Name]</span>
      <span data-lang="pt">[Portuguese Name]</span>
    </h4>
  </div>
  <div class="exception-card__body">
    <div class="exception-card__trigger">
      <strong><span data-lang="en">Trigger:</span><span data-lang="pt">Gatilho:</span></strong>
      <span data-lang="en">[When this occurs]</span>
      <span data-lang="pt">[Portuguese description]</span>
    </div>
    <div class="exception-card__resolution">
      <strong><span data-lang="en">Resolution:</span><span data-lang="pt">Resolução:</span></strong>
      <ol>
        <li><span data-lang="en">[Step 1]</span><span data-lang="pt">[Portuguese]</span></li>
        <li><span data-lang="en">[Step 2]</span><span data-lang="pt">[Portuguese]</span></li>
      </ol>
    </div>
    <div class="exception-card__escalation">
      <strong><span data-lang="en">Escalate to:</span><span data-lang="pt">Escalar para:</span></strong>
      <span>[Role/Contact]</span>
    </div>
  </div>
</div>
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

### Exception Handling
- Anticipate common failure modes
- Provide clear recovery steps
- Define escalation criteria
- Include contact information
