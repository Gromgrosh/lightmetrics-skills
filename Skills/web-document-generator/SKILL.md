---
name: web-document-generator
description: Generate professional B2B technical documents (installation guides, product specs, process workflows, technical manuals) as self-contained HTML files with multi-language support. Use this skill when the user asks to create documentation, write a user guide, build an installation guide, generate technical specs, create process workflows, or produce any professional technical document for internal or external use. Also use when the user mentions "web document", "HTML guide", "technical documentation", or wants to create bilingual/multilingual documentation.
---

# Web Document Generator

Create professional B2B technical documents as self-contained HTML files with configurable language support. This skill guides you through a structured 8-phase workflow from discovery to delivery.

> **IMPORTANT — Start here:** When this skill activates, ALWAYS begin at the **Getting Started** section below. Do NOT skip ahead to Phase 1. Present the entry-point menu first using `AskUserQuestion` so the user can choose between creating a document or learning how the skill works.

## Document Types

- **Installation Guide** — Step-by-step procedures for setting up hardware/software
- **Product Specification** — Technical details, features, and requirements
- **Process Workflow** — Business or technical process documentation
- **Technical Manual** — Comprehensive reference documentation

## Workflow Overview

The document creation process follows 8 phases with clear handoffs:

| Phase | Name | Purpose |
|-------|------|---------|
| 1 | Discovery Interview | Understand requirements, create document brief |
| 2 | Structure Blueprint | Design content architecture |
| 3 | Content Drafting | Write and approve full content + translations |
| 4 | Content Assembly | Gather assets, screenshots, images |
| 5 | Draft Generation | Build initial HTML document |
| 6 | Review Cycle | Iterative feedback and revision |
| 7 | Output Production | Finalize and validate |
| 8 | Delivery & Handoff | Package for distribution |

---

## Getting Started

When the skill activates, use `AskUserQuestion` to present two paths:

| # | Question | Header | Options |
|---|----------|--------|---------|
| 1 | "What would you like to do?" | `Get started` | **Create a document** — Start the 8-phase workflow to build a new technical document · **How to use this skill** — See a walkthrough of the full process before starting |

- If **Create a document** → proceed to Phase 1.
- If **How to use this skill** → present the guide below. **Do NOT immediately ask a follow-up question or prompt the user to start.** End your message after displaying the guide and let the user read at their own pace. Only proceed to Phase 1 when the user explicitly says they're ready (e.g., "let's start", "create a document", "ready").

---

## How to Use This Skill

A walkthrough of the entire document creation process so you know what to expect.

### Before You Start

Have these ready before beginning:

- [ ] **Content scope** — what the document covers, and what's explicitly out of scope
- [ ] **Target audience** — who will read this and their technical level
- [ ] **Languages** — which languages the document needs to support
- [ ] **Image sources** — Figma design URLs, FigJam board URLs, and/or local image files
- [ ] **Reference materials** — existing docs, specs, or content to build from

### Phase-by-Phase Walkthrough

| Phase | What Claude Does | What You Provide | Key Artifacts | Approval Point |
|-------|-----------------|-------------------|---------------|----------------|
| **1. Discovery** | Asks interactive questions in 2 batches | Pick from choices or type custom answers, provide a doc name | `context.md` | Approve the Document Brief |
| **2. Structure** | Proposes section outline based on template | Review, reorder, add/remove sections | `structure.md` | Approve the structure |
| **3. Content Drafting** | Writes complete text for every section, then generates translations for each requested language | Review primary language text section-by-section, then review translations | `final_content.md`, `final_content_{lang}.md` | Approve content + translations |
| **4. Content Assembly** | Extracts images from Figma/FigJam/manual sources, applies naming convention, builds manifest | Provide URLs and file paths, confirm renaming table and image-to-section mapping | `assets/`, `image-manifest.json`, `content-status.md` | Confirm image mapping |
| **5. Draft Generation** | Builds full HTML from approved content + images | Review in browser | `draft-v1.html` | Review the draft |
| **6. Review Cycle** | Makes targeted revisions from your feedback | Provide feedback (content, style, structure, assets) | `draft-v{N}.html`, `revision-log.md` | Mark "Ready for output" |
| **7. Output** | Validates accessibility, images, links; generates quality report | Review final output | `final/index.html`, `quality-report.md` | Approve final |
| **8. Delivery** | Packages into `dist/` folder with README and maintenance guide | Share with team | `dist/` folder | Done |

### Document Types Explained

| Type | Best For | Example |
|------|----------|---------|
| **Installation Guide** | Step-by-step hardware/software setup with numbered steps and screenshots | "RideView Device Installation Guide" |
| **Product Specification** | Technical details, features, requirements, compatibility matrices | "RideView Camera Specifications" |
| **Process Workflow** | Business processes, approval flows, RACI matrices | "Fleet Onboarding Process" |
| **Technical Manual** | Comprehensive reference docs, API guides, admin procedures | "RideView Platform Admin Manual" |

### Content Collection: What to Prepare

The skill supports **3 image source types**:

| Source | How to Provide | What Happens |
|--------|---------------|--------------|
| **Figma design URLs** | Paste `figma.com/design/...` links | Claude extracts screenshots automatically via MCP tools |
| **FigJam board URLs** | Paste `figma.com/board/...` links | Claude extracts diagrams and flow images via MCP tools |
| **Local image files** | Paste file paths or drag/drop images into the conversation | Claude copies and renames them into the project `assets/` folder |

**During Phase 4 (Content Assembly):**
1. Claude classifies all your sources
2. Extracts images and auto-renames them using a strict convention (e.g., `s1_0-device-overview.jpg` for Step 1 of an Installation Guide)
3. Presents a mapping table showing which image goes in which section, with what layout (full-width or side-by-side)
4. You confirm or adjust before proceeding

**Tip:** Provide Figma and FigJam links early in Phase 1 so Claude can reference designs during structure planning (Phase 2) and content writing (Phase 3).

### Tips & Best Practices

- **Provide all image links upfront** in Discovery — it helps Claude plan the structure around them
- **Keep scope tight** — one document per workflow run works best
- **Consolidate feedback** into a single round when possible (Phase 6 warns at 5+ iterations)
- **Use "Other"** in interactive questions for custom answers beyond the predefined choices
- **For multilingual docs**, review translations carefully in Phase 3 — native speaker review is ideal
- **Content before images** — the full text is written and approved (Phase 3) before images are assembled (Phase 4), so content changes don't require re-mapping images

### Resuming a Session

If a conversation is interrupted, start a new session and point Claude to the project folder. Claude detects the current phase by checking which artifacts exist:

| Artifacts Found | Resume At |
|-----------------|-----------|
| Only `context.md` | Phase 2 — Structure Blueprint |
| `context.md` + `structure.md` | Phase 3 — Content Drafting |
| `structure.md` + `final_content.md` | Phase 4 — Content Assembly |
| `final_content.md` + `image-manifest.json` | Phase 5 — Draft Generation |
| `draft-v{N}.html` exists | Phase 6 — Review Cycle |
| `quality-report.md` exists | Phase 8 — Delivery & Handoff |

### Output

The final deliverable is:
- **Self-contained HTML** — all CSS embedded in `<style>` tags, images in `./assets/`
- **Multi-language toggle** in the header (if configured)
- **Responsive** — mobile (<640px), tablet (640-1199px), desktop (≥1200px)
- **Accessible** — alt text on all images, correct heading hierarchy, WCAG AA contrast
- **Packaged** in a `dist/` folder ready to share with your dev team

---

## Phase 1: Discovery Interview

**Goal**: Understand the document requirements and create a resumable project folder.

### Actions

All discovery questions use the `AskUserQuestion` tool for an interactive experience. Each question provides relevant predefined choices — the user can pick one or select "Other" to type a custom answer. Questions are grouped into batches of up to 4 (the tool's limit per call).

**Batch 1 — Document basics:**

Use `AskUserQuestion` with these 4 questions:

| # | Question | Header | Options |
|---|----------|--------|---------|
| 1 | "What type of document do you want to create?" | `Doc type` | **Installation Guide** — Step-by-step setup procedures for hardware/software · **Product Specification** — Technical details, features, and requirements · **Process Workflow** — Business or technical process documentation · **Technical Manual** — Comprehensive reference documentation |
| 2 | "What is the purpose of this document?" | `Purpose` | **Onboard new users** — Help users get started with a product or system · **Internal reference** — Technical documentation for internal teams · **Customer-facing guide** — External documentation shipped to customers · **Compliance / audit** — Required documentation for regulatory or process compliance |
| 3 | "Who is the primary audience?" | `Audience` | **Field installers / technicians** — Hands-on workers doing physical setup · **End users / non-technical** — Everyday users who need clear, simple guidance · **Developers / engineers** — Technical staff integrating or maintaining systems · **Managers / stakeholders** — Decision-makers needing overview-level information |
| 4 | "What is the audience's technical level?" | `Tech level` | **Beginner** — Needs detailed step-by-step guidance with screenshots · **Intermediate** — Familiar with the domain, needs reference-level detail · **Advanced** — Expert-level, needs API specs, configs, and edge cases |

**Batch 2 — Scope and assets:**

Use `AskUserQuestion` with these 3 questions:

| # | Question | Header | Options |
|---|----------|--------|---------|
| 5 | "Which languages should the document support?" | `Languages` | **English only** — Single language document · **English + Portuguese** — Bilingual with language toggle · **English + Spanish** — Bilingual with language toggle · **English + Portuguese + Spanish** — Trilingual with language toggle |
| 6 | "What image sources will you provide?" | `Assets` | **Figma design URLs** — Screenshots from Figma design files · **FigJam board URLs** — Diagrams and flows from FigJam boards · **Local image files** — File paths or images pasted into conversation · **No images yet** — Will add images later |
| 7 | "Give this document a short name (used for the project folder, e.g. 'rideview-install-guide')" | `Doc name` | *(No predefined options — use a single free-text question. Ask as a follow-up message, not via AskUserQuestion, since this always needs a custom answer.)* |

> **Note on question 6:** Enable `multiSelect: true` so the user can select multiple asset source types.

> **Note on question 7:** Ask this as a plain text follow-up after the two AskUserQuestion batches, since it always requires a custom answer.

After collecting all answers:

1. **Generate a Document Brief** summarizing all answers in a clear format:

   ```markdown
   ## Document Brief
   - **Type:** Installation Guide
   - **Purpose:** Onboard new users — help field installers set up the device
   - **Audience:** Field installers / technicians (Beginner level)
   - **Languages:** English + Portuguese
   - **Assets:** Figma design URLs, Local image files
   - **Document name:** rideview-install-guide
   ```

2. **Present the brief for approval** before creating any files.

3. **Create project folder and context file** (only after approval):
   ```
   [document-name]/
   ├── context.md         # Discovery answers for resumability
   └── assets/            # Will hold images and resources
   ```

4. **Save all answers to `context.md`** so the session can be resumed.

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

## Phase 3: Content Drafting

**Goal**: Write the complete document content as markdown in the primary language, get user approval, then generate all requested language translations.

### Actions

1. **Read approved `structure.md`** and the writing guidelines (`references/writing-guidelines.md`).

2. **Draft full content for every section** into `final_content.md` (primary language first):
   - Complete prose — headings, body text, callouts, decision tables, step-by-step instructions
   - Follow writing guidelines: imperative verbs, active voice, progressive disclosure
   - Use `[IMAGE: description]` placeholders where screenshots or diagrams will be inserted later
   - Mark callout types inline: `[WARNING: text]`, `[INFO: text]`, `[CONDITIONAL: text]`, `[SUCCESS: text]`

3. **Present the content for review** section by section:
   - User can approve, edit, or request rewrites per section
   - Track approval status per section within the file

4. **Finalize primary language content** once all sections are approved.

5. **Generate language translations** (based on languages selected in Phase 1):
   - For each additional language (e.g., Portuguese, Spanish):
     - Translate the approved `final_content.md` content
     - Translate meaning, not just words — adapt idioms, maintain professional tone
     - Preserve `[IMAGE: ...]` placeholders and `[WARNING]`/`[INFO]` markers as-is (these are not translated)
     - Write to `final_content_{lang}.md` (e.g., `final_content_pt.md`, `final_content_es.md`)
   - Present translations for user review (user or native speaker can approve/edit)
   - If only one language was selected in Discovery, skip this step

6. **Finalize all language files** once translations are approved.

### Artifacts
- `[document-name]/final_content.md` — approved primary language content with image placeholders
- `[document-name]/final_content_{lang}.md` — approved translation per additional language (if multilingual)

### Handoff
User approves all content + translations → Phase 4

---

## Phase 4: Content Assembly

**Goal**: Gather all assets and content needed for the document.

### Actions

> All image extraction follows the **Image Rules Reference** appendix at the end of this document. Refer to it for URL parsing, tool selection, naming conventions, and the manifest schema.

1. **Classify image sources**:
   - Scan `final_content.md` for `[IMAGE: ...]` placeholders and cross-reference with links/files provided during Discovery (Phase 1)
   - Classify each as one of three source types:
     - `figma-design` — Figma design file URLs (`figma.com/design/...`)
     - `figjam-board` — FigJam board URLs (`figma.com/board/...`)
     - `manual` — Local file paths or images pasted/dragged into conversation
   - Parse each URL to extract `fileKey` and `nodeId` (see **Image Rules Reference → URL Parsing**)
   - Present the classified list to the user for confirmation before extracting

2. **Extract Figma design screenshots** (for each `figma-design` source):
   - Parse the URL to get `fileKey` and `nodeId`
   - Select the appropriate MCP tool (see **Image Rules Reference → Tool Selection Matrix**):
     - **Preferred**: `get_design_context(fileKey, nodeId)` via web API — returns screenshot + context
     - **Fallback**: `get_screenshot(fileKey, nodeId)` via web API — screenshot only
     - **Desktop**: `mcp__Figma__get_screenshot(nodeId)` — if user has desktop app open
   - Save the extracted image to `[document-name]/assets/` using the naming convention
   - Log the source URL, fileKey, nodeId, and tool used in the manifest

3. **Extract FigJam board images** (for each `figjam-board` source):
   - Parse the board URL to get `fileKey` and `nodeId`
   - Use `get_figjam(fileKey, nodeId)` via web API MCP with `includeImagesOfNodes: true`
   - Save extracted node images to `[document-name]/assets/` using the naming convention
   - FigJam images are typically diagrams, flowcharts, or process maps — name accordingly using `diag_` prefix if they don't map to a specific section

4. **Process manual images** (for each `manual` source):
   - **File paths** (e.g., `/Users/.../screenshot.png`):
     - Validate the file exists at the given path
     - Copy to `[document-name]/assets/` with the naming convention applied
     - Log `originalPath` and `method: "file-path"` in the manifest
   - **Pasted/dragged images** (provided directly in conversation):
     - Save the image data to `[document-name]/assets/` as a file
     - Apply the naming convention
     - Log `method: "pasted"` in the manifest
   - If a file path is not found, warn the user immediately and mark the entry as `failed`

5. **Apply naming convention** to all collected images:
   - Follow the strict naming pattern from **Image Rules Reference → Naming Convention**:
     - Pattern: `{prefix}{N}_{sub}-{description}.{ext}`
     - Prefix depends on document type: `s` (Installation Guide), `sec` (Product Spec), `stg` (Process Workflow), `ch` (Technical Manual)
     - `_0` = section overview/primary image; `_1`, `_2` = sub-images
     - Special prefixes for non-section images: `hero_`, `diag_`, `ref_`, `exc_`
   - Present a renaming table to the user showing: original filename → new filename → target section
   - Apply renames only after user confirms

6. **Build image manifest** (`image-manifest.json`):
   - Use the v2.0 schema (see **Image Rules Reference → Manifest Schema**)
   - Each entry must include: `filename`, `alt`, `section`, `layout` (full-width or side-by-side), full `source` provenance, `status`, and `extractedAt` timestamp
   - Write to `[document-name]/image-manifest.json`

7. **Link images to sections**:
   - Cross-reference images against `structure.md` sections
   - Present an interactive mapping table to the user:

     | Image | Section | Alt Text | Layout |
     |-------|---------|----------|--------|
     | `s1_0-device-unboxing.jpg` | Step 1: Unboxing | Device unboxing showing all components | full-width |
     | `s1_1-power-cable.png` | Step 1: Unboxing | Power cable connection detail | side-by-side |

   - User confirms or adjusts: section assignment, alt text, and layout choice
   - Update manifest with confirmed mappings

8. **Present assembly status**:
   - Summary counts: X Figma screenshots, X FigJam images, X manual images
   - Any failed extractions with reasons
   - Sections still missing images (from structure.md)
   - Generate `[document-name]/content-status.md` with per-section status: ready | needs-input | blocked

### Artifacts
- `[document-name]/assets/` — all images
- `[document-name]/image-manifest.json`
- `[document-name]/content-status.md`

### Handoff
Critical content collected → Phase 5

---

## Phase 5: Draft Generation

**Goal**: Build the complete HTML document from approved content and assembled images.

### Actions

1. **Read design tokens**:
   - Load `references/design-tokens.md` for styling
   - Apply Light Spectrum color palette and typography

2. **Apply document type template**:
   - Read `references/templates/[type].md`
   - Structure HTML according to template patterns

3. **Generate section-by-section HTML**:
   - Read `final_content.md` (and `final_content_{lang}.md` for translations) — do NOT regenerate content, use the approved text
   - For each section in final_content.md:
     - Purpose statement
     - Step-by-step actions
     - Decision points
     - Screenshots with captions
   - **Image placement**: Read `image-manifest.json` and use the `layout` field to select the HTML pattern:
     - `full-width` → `<figure class="image-container">` wrapper
     - `side-by-side` → `<div class="screenshot-panel">` wrapper
   - Use the manifest `alt` text for every `<img>` tag
   - See **Image Rules Reference → HTML Referencing Patterns** for exact markup

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
User reviews draft → Phase 6

---

## Phase 6: Review Cycle (Iterative)

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
User marks "Ready for output" → Phase 7

---

## Phase 7: Output Production

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
User reviews final → Phase 8

---

## Phase 8: Delivery & Handoff

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
- `final_content.md` — Contains approved primary language content
- `final_content_{lang}.md` — Contains approved translations
- `image-manifest.json` — Contains image assembly state
- `feedback-document.md` — Contains outstanding feedback items
- Latest `draft-v{N}.html` — Current document state

When resuming, identify the current phase by checking which artifacts exist (see **How to Use This Skill → Resuming a Session** for the detection table).

---

## Quick Reference

### Image Extraction
See the **Image Rules Reference** appendix below for complete details on:
- URL parsing (Figma design, FigJam board, branch URLs)
- MCP tool selection matrix
- Naming conventions per document type
- Image manifest v2.0 schema
- HTML referencing patterns
- Validation checks and error handling

### Language Switching Pattern
```html
<span data-lang="en">English text</span>
<span data-lang="pt">Portuguese text</span>
```

### Self-Contained HTML
All styles must be embedded in `<style>` tags. All images should be referenced from relative `./assets/` path or embedded as base64 for true single-file output.

---

## Image Rules Reference

Comprehensive rules for extracting, naming, organizing, and referencing images from all supported source types.

### URL Parsing

Extract `fileKey` and `nodeId` from URLs before calling any MCP tool:

| URL Type | Pattern | Extraction |
|----------|---------|------------|
| **Figma Design** | `https://figma.com/design/{fileKey}/{fileName}?node-id={int1}-{int2}` | `fileKey` = `{fileKey}`, `nodeId` = `{int1}:{int2}` (convert hyphen to colon) |
| **Figma Branch** | `https://figma.com/design/{fileKey}/branch/{branchKey}/{fileName}` | `fileKey` = `{branchKey}` (use branch key, NOT the main file key) |
| **FigJam Board** | `https://figma.com/board/{fileKey}/{fileName}?node-id={int1}-{int2}` | `fileKey` = `{fileKey}`, `nodeId` = `{int1}:{int2}` |

**Critical:** The `node-id` query parameter uses a hyphen (`1-2`) but MCP tools expect a colon (`1:2`). Always convert.

### Tool Selection Matrix

Choose the MCP tool based on what's available and what's needed:

| Scenario | Tool | Required Params | Returns |
|----------|------|-----------------|---------|
| Figma URL provided (preferred) | `mcp__a8305967…__get_design_context` | `fileKey`, `nodeId` | Screenshot + code + asset URLs |
| Figma URL, screenshot only | `mcp__a8305967…__get_screenshot` | `fileKey`, `nodeId` | Screenshot only |
| Figma desktop app open | `mcp__Figma__get_screenshot` | `nodeId` (optional, uses selection) | Screenshot only |
| Figma desktop + need context | `mcp__Figma__get_design_context` | `nodeId` (optional) | Screenshot + code + metadata |
| FigJam board URL | `mcp__a8305967…__get_figjam` | `fileKey`, `nodeId`, `includeImagesOfNodes: true` | Node images + structure |

**Selection priority:**
1. If user provides a URL → use the web API tools (`mcp__a8305967…`)
2. If user says "current selection" or desktop is open → use desktop tools (`mcp__Figma__`)
3. Prefer `get_design_context` over `get_screenshot` (richer output)
4. FigJam boards always use `get_figjam` — `get_screenshot` does not work for boards

### Naming Convention

**Pattern:** `{prefix}{N}_{sub}-{description}.{ext}`

#### Document-Type Prefixes

| Document Type | Prefix | Meaning | Examples |
|---------------|--------|---------|---------|
| Installation Guide | `s` | Step | `s1_0-unboxing-overview.jpg`, `s3_2-cable-routing.png` |
| Product Spec | `sec` | Section | `sec1_0-system-architecture.png`, `sec2_1-hardware-dims.svg` |
| Process Workflow | `stg` | Stage | `stg1_0-request-form.jpg`, `stg3_1-approval-screen.png` |
| Technical Manual | `ch` | Chapter | `ch1_0-dashboard-overview.png`, `ch4_2-api-response.png` |

#### Special Prefixes (for images outside normal sections)

| Prefix | Use Case | Examples |
|--------|----------|---------|
| `hero_` | Hero banner / document header image | `hero_product-front.jpg` |
| `diag_` | Diagrams, flowcharts, architecture maps | `diag_system-flow.svg`, `diag_network-topology.png` |
| `ref_` | Reference images, legends, keys | `ref_led-status-codes.png` |
| `exc_` | Exception / error state screenshots | `exc_connection-timeout.png` |

#### Naming Rules

- `_0` = primary/overview image for that section
- `_1`, `_2`, `_3` etc. = subsequent images within the same section, in order of appearance
- Description: **lowercase**, **hyphens** between words, **max 4 words**
- Preserve the original file extension (`.jpg`, `.png`, `.svg`, `.webp`)
- No spaces, no uppercase, no special characters beyond hyphens in description

#### Full Example (Installation Guide with 3 steps)

```
assets/
├── hero_rideview-product.jpg
├── s1_0-unboxing-overview.jpg
├── s1_1-package-contents.png
├── s1_2-power-adapter-detail.png
├── s2_0-mounting-position.jpg
├── s2_1-bracket-alignment.png
├── s3_0-app-home-screen.png
├── s3_1-wifi-connection.png
├── s3_2-device-pairing.png
├── diag_connection-flow.svg
└── ref_led-indicators.png
```

### Image Manifest Schema (v2.0)

The manifest tracks every image with full provenance and status:

```json
{
  "version": "2.0",
  "documentType": "installation-guide",
  "images": [
    {
      "filename": "s1_0-unboxing-overview.jpg",
      "alt": "Device unboxing showing all included components laid out",
      "section": "Step 1: Unboxing",
      "layout": "full-width",
      "source": {
        "type": "figma-design",
        "url": "https://figma.com/design/abc123/MyFile?node-id=1-2",
        "fileKey": "abc123",
        "nodeId": "1:2",
        "tool": "get_design_context"
      },
      "status": "confirmed",
      "extractedAt": "2026-04-03T10:30:00Z"
    },
    {
      "filename": "s2_0-mounting-position.jpg",
      "alt": "Recommended mounting position on windshield",
      "section": "Step 2: Mounting",
      "layout": "side-by-side",
      "source": {
        "type": "manual",
        "originalPath": "/Users/mohit/Desktop/mounting-photo.jpg",
        "method": "file-path"
      },
      "status": "confirmed",
      "extractedAt": "2026-04-03T10:35:00Z"
    },
    {
      "filename": "diag_connection-flow.svg",
      "alt": "Device connection flow showing WiFi and Bluetooth steps",
      "section": "Overview",
      "layout": "full-width",
      "source": {
        "type": "figjam-board",
        "url": "https://figma.com/board/xyz789/FlowBoard?node-id=5-10",
        "fileKey": "xyz789",
        "nodeId": "5:10",
        "tool": "get_figjam"
      },
      "status": "confirmed",
      "extractedAt": "2026-04-03T10:40:00Z"
    }
  ]
}
```

**Field reference:**

| Field | Required | Values | Purpose |
|-------|----------|--------|---------|
| `filename` | Yes | Named per convention | Final filename in `assets/` |
| `alt` | Yes | Descriptive text | Accessibility alt text |
| `section` | Yes | Matches `structure.md` | Which document section uses this image |
| `layout` | Yes | `full-width` or `side-by-side` | Determines HTML pattern in Phase 4 |
| `source.type` | Yes | `figma-design`, `figjam-board`, `manual` | Source classification |
| `source.url` | If Figma/FigJam | Original URL | Traceability |
| `source.fileKey` | If Figma/FigJam | Extracted from URL | Re-extraction if needed |
| `source.nodeId` | If Figma/FigJam | Extracted from URL | Re-extraction if needed |
| `source.tool` | If Figma/FigJam | Tool name used | Debugging |
| `source.originalPath` | If manual file-path | Absolute path | Traceability |
| `source.method` | If manual | `file-path` or `pasted` | How user provided the image |
| `status` | Yes | `pending`, `extracted`, `confirmed`, `failed` | Workflow tracking |
| `extractedAt` | Yes | ISO 8601 timestamp | When image was captured |

### HTML Referencing Patterns

Phase 5 reads the manifest `layout` field to select the correct HTML pattern:

**`full-width`** — Use for overview images, diagrams, wide screenshots:
```html
<figure class="image-container">
  <img
    src="./assets/s1_0-unboxing-overview.jpg"
    alt="Device unboxing showing all included components"
    loading="lazy"
  />
</figure>
```

**`side-by-side`** — Use for mobile screenshots, detail crops, inline visuals:
```html
<div class="screenshot-panel">
  <div class="screenshot-panel__wrap">
    <img
      src="./assets/s3_0-app-home-screen.png"
      alt="App home screen with installation button highlighted"
      class="screenshot-panel__img"
      loading="lazy"
    />
  </div>
  <p class="screenshot-panel__caption">App home screen</p>
</div>
```

**Rules for all images:**
- Images are **NOT** clickable (no zoom interaction)
- Always include `loading="lazy"`
- Always include descriptive `alt` text from the manifest
- Use relative paths: `./assets/{filename}`
- Image containers have a light-tinted background (handled by CSS)

### Validation Checks

Run these checks during Phase 7 (Output Production):

| Check | Applies To | Severity |
|-------|-----------|----------|
| Alt text present and non-empty | All images | Error |
| File exists in `assets/` | All images | Error |
| Filename follows naming convention | All images | Warning |
| `layout` field matches HTML pattern used | All images | Warning |
| Source URL is still accessible | Figma/FigJam | Info |
| `originalPath` logged in manifest | Manual (file-path) | Info |
| No duplicate filenames | All images | Error |
| Image referenced in HTML matches manifest | All images | Error |

### Error Handling

| Failure | Action |
|---------|--------|
| Figma extraction fails (auth, network, invalid node) | Log error, set `status: "failed"`, flag for user attention, suggest re-sharing the URL or providing a manual screenshot |
| FigJam extraction returns no images | Set `status: "failed"`, suggest user export manually from FigJam and provide as file path |
| File path not found | Warn user immediately, set `status: "failed"`, ask for corrected path |
| Pasted image cannot be saved | Instruct user to save the image locally and provide the file path instead |
| Image is too large (>5MB) | Warn user, suggest compressing or using a different format |
| Unsupported format | Warn user, only `.jpg`, `.png`, `.svg`, `.webp` are supported |
