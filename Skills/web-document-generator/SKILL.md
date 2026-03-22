---
name: web-document-generator
description: Generate professional B2B technical documents (installation guides, product specs, process workflows, technical manuals) as self-contained HTML files with multi-language support. Use this skill when the user asks to create documentation, write a user guide, build an installation guide, generate technical specs, create process workflows, or produce any professional technical document for internal or external use. Also use when the user mentions "web document", "HTML guide", "technical documentation", or wants to create bilingual/multilingual documentation.
---

# Web Document Generator

Create professional B2B technical documents as self-contained HTML files with configurable language support. This skill guides you through a structured 7-phase workflow from discovery to delivery.

## Document Types

- **Installation Guide** — Step-by-step procedures for setting up hardware/software
- **Product Specification** — Technical details, features, and requirements
- **Process Workflow** — Business or technical process documentation
- **Technical Manual** — Comprehensive reference documentation

## Workflow Overview

The document creation process follows 7 phases with clear handoffs:

| Phase | Name | Purpose |
|-------|------|---------|
| 1 | Discovery Interview | Understand requirements, create document brief |
| 2 | Structure Blueprint | Design content architecture |
| 3 | Content Assembly | Gather assets, screenshots, content |
| 4 | Draft Generation | Build initial HTML document |
| 5 | Review Cycle | Iterative feedback and revision |
| 6 | Output Production | Finalize and validate |
| 7 | Delivery & Handoff | Package for distribution |

---

## Phase 1: Discovery Interview

**Goal**: Understand the document requirements and create a resumable project folder.

### Actions

1. Present document type options:
   - Installation Guide
   - Product Specification
   - Process Workflow
   - Technical Manual

2. Ask structured questions:
   - **Purpose**: What is this document for? Who will use it?
   - **Audience**: Technical level? Field installers, end users, developers?
   - **Scope**: What does it cover? What's explicitly out of scope?
   - **Languages**: Which languages are required? (e.g., English + Portuguese)
   - **Assets**: Are there Figma designs, existing docs, or screenshots to use?

3. Generate a Document Brief summarizing all answers.

4. Create project folder and context file:
   ```
   [document-name]/
   ├── context.md         # Discovery info for resumability
   └── assets/            # Will hold images and resources
   ```

### Artifacts
- `[document-name]/` folder created
- `[document-name]/context.md` — captures all discovery info

### Handoff
User approves the Document Brief → Phase 2

---

## Phase 2: Structure Blueprint

**Goal**: Design the document's content architecture.

### Actions

1. Analyze any provided source materials:
   - Figma URLs → use Figma MCP to understand design
   - Existing docs → extract structure patterns
   - Reference materials → identify content sections

2. Propose document structure based on the document type template:
   - Read the appropriate template from `references/templates/`
   - Adapt sections to user's specific needs

3. Write structure as markdown file (content-level, no HTML yet).

4. Present structure for review with these options:
   - Approve as-is
   - Reorder sections
   - Add/remove sections
   - Mark which sections need Claude's help vs user-provided content

### Artifacts
- `[document-name]/structure.md` — content-level structure

### Handoff
User approves structure → Phase 3

---

## Phase 3: Content Assembly

**Goal**: Gather all assets and content needed for the document.

### Actions

1. **Extract Figma screenshots** (if URLs provided):
   - Use `mcp__claude_ai_Figma__get_screenshot` for design captures
   - Save to `assets/` directory with descriptive names

2. **Process manual file paths**:
   - Copy referenced images to `assets/`
   - Validate file existence

3. **Build image manifest**:
   ```json
   {
     "images": [
       {
         "filename": "step-1-overview.png",
         "alt": "Installation overview screen",
         "section": "Step 1",
         "source": "figma" | "manual"
       }
     ]
   }
   ```

4. **Generate content checklist**:
   - List each section needing content
   - Mark status: ready | needs-input | blocked

5. **Present assembly status** to user.

### Artifacts
- `[document-name]/assets/` — all images
- `[document-name]/image-manifest.json`
- `[document-name]/content-status.md`

### Handoff
Critical content collected → Phase 4

---

## Phase 4: Draft Generation

**Goal**: Build the complete HTML document.

### Actions

1. **Read design tokens**:
   - Load `references/design-tokens.md` for styling
   - Apply Light Spectrum color palette and typography

2. **Apply document type template**:
   - Read `references/templates/[type].md`
   - Structure HTML according to template patterns

3. **Generate section-by-section content**:
   - For each section in structure.md:
     - Purpose statement
     - Step-by-step actions
     - Decision points
     - Screenshots with captions

4. **Handle language variants**:
   - Use `data-lang` attributes for multi-language content
   - Generate language selector UI

5. **Build complete HTML**:
   - Self-contained with embedded CSS
   - Responsive layout
   - Accessible markup

6. **Open draft in browser** for preview:
   ```bash
   open [document-name]/draft-v1.html
   ```

### Artifacts
- `[document-name]/draft-v1.html`

### Handoff
User reviews draft → Phase 5

---

## Phase 5: Review Cycle (Iterative)

**Goal**: Refine the document based on user feedback.

### Actions

1. **Create feedback document**:
   - Convert user feedback into checklist format
   - Categorize: content | style | structure | assets

2. **Make targeted revisions**:
   - Preserve approved sections
   - Only modify sections with feedback
   - Track changes made

3. **Update feedback checklist**:
   - Check off items as addressed
   - Note any items requiring clarification

4. **Track iteration count**:
   - Warn if approaching 5+ iterations
   - Suggest consolidating remaining feedback

5. **Open updated preview** for review.

### Artifacts
- `[document-name]/feedback-document.md`
- `[document-name]/draft-v{N}.html`
- `[document-name]/revision-log.md`

### Handoff
User marks "Ready for output" → Phase 6

---

## Phase 6: Output Production

**Goal**: Finalize the document for distribution.

### Actions

1. **Finalize HTML**:
   - Remove any draft indicators
   - Optimize image references
   - Minify CSS (optional)

2. **Validate accessibility**:
   - All images have alt text
   - Heading hierarchy is correct
   - Color contrast meets WCAG AA

3. **Generate language-specific versions** (if configured):
   - Create separate files or use single file with language toggle

4. **Run quality checks**:
   - Verify all images exist
   - Check internal links
   - Validate HTML structure

5. **Generate quality report**:
   ```markdown
   ## Quality Report
   - Images: X/X present
   - Alt text: X/X complete
   - Links: X/X valid
   - Languages: [list]
   ```

### Artifacts
- `[document-name]/final/index.html`
- `[document-name]/quality-report.md`

### Handoff
User reviews final → Phase 7

---

## Phase 7: Delivery & Handoff

**Goal**: Package for distribution and handoff to dev team.

### Actions

1. **Create distribution folder**:
   ```
   [document-name]/dist/
   ├── index.html
   ├── assets/
   │   └── [all images]
   └── README.md
   ```

2. **Generate delivery summary**:
   - File locations
   - Language versions included
   - Usage instructions

3. **Create maintenance guide**:
   - How to update content
   - Where to find source files
   - Contact for questions

4. **Package for sharing**:
   - Optionally create ZIP archive
   - Verify all files included

### Artifacts
- `[document-name]/dist/` — shareable folder
- `[document-name]/delivery-summary.md`
- `[document-name]/maintenance-guide.md`

### Handoff
User shares `dist/` folder with dev team for deployment.

---

## Reference Files

### Templates
Read the appropriate template based on document type:
- `references/templates/installation-guide.md` — for step-by-step installation procedures
- `references/templates/product-spec.md` — for technical specifications
- `references/templates/process-workflow.md` — for business/technical processes
- `references/templates/technical-manual.md` — for comprehensive reference docs

### Design System
- `references/design-tokens.md` — Light Spectrum colors, typography, spacing
- `assets/base-styles.css` — Base CSS for all documents

### Writing Guidelines
- `references/writing-guidelines.md` — Style guide for content

### Scripts
- `scripts/generate_html.py` — HTML generation utilities
- `scripts/validate_document.py` — Quality validation

---

## Resume Support

If a session is abandoned, the skill can resume using:
- `context.md` — Contains discovery interview answers
- `structure.md` — Contains approved document structure
- `feedback-document.md` — Contains outstanding feedback items
- Latest `draft-v{N}.html` — Current document state

When resuming, identify the current phase by checking which artifacts exist and their state.

---

## Quick Reference

### Figma Screenshot Extraction
```
Use mcp__claude_ai_Figma__get_screenshot with:
- fileKey: extracted from Figma URL
- nodeId: specific frame or component ID
- scale: 2 for high-res captures
```

### Language Switching Pattern
```html
<span data-lang="en">English text</span>
<span data-lang="pt">Portuguese text</span>
```

### Self-Contained HTML
All styles must be embedded in `<style>` tags. All images should be referenced from relative `./assets/` path or embedded as base64 for true single-file output.
