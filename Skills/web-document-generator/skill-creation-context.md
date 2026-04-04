# Web Document Generator Skill — Creation Context

**Created:** 2026-03-22
**Location:** `/Users/mohit/claude-workspace/projects/Lightmetrics/web-document-generator`
**Status:** Implemented and tested

---

## Overview

A Claude Code skill for generating professional B2B technical documents (installation guides, product specs, process workflows, technical manuals) as self-contained HTML files with multi-language support.

---

## Skill Structure

```
web-document-generator/
├── SKILL.md                          # Main skill definition (7-phase workflow)
├── references/
│   ├── templates/
│   │   ├── installation-guide.md     # Step-by-step installation procedures
│   │   ├── product-spec.md           # Technical specifications
│   │   ├── process-workflow.md       # Business/technical processes
│   │   ├── technical-manual.md       # Comprehensive reference docs
│   │   └── common-template-spec.md   # Shared header/sidebar/layout specs
│   ├── template-comparison.md        # Structural comparison of all 4 templates
│   ├── design-tokens.md              # Light Spectrum colors, typography, spacing
│   └── writing-guidelines.md         # Style guide for content
├── scripts/
│   ├── generate_html.py              # HTML generation utilities
│   └── validate_document.py          # Quality validation checks
└── assets/
    ├── base-styles.css               # Base CSS with all design tokens
    └── brand/
        ├── brand_lightmetrics-logo.webp  # Lightmetrics logo
        └── brand_rideview-logo.svg       # RideView logo
```

---

## Key Features

### 7-Phase Workflow
1. **Discovery Interview** — Understand requirements, create document brief
2. **Structure Blueprint** — Design content architecture
3. **Content Assembly** — Gather assets, screenshots, content
4. **Draft Generation** — Build initial HTML document
5. **Review Cycle** — Iterative feedback and revision
6. **Output Production** — Finalize and validate
7. **Delivery & Handoff** — Package for distribution

### Document Types
- Installation Guide
- Product Specification
- Process Workflow
- Technical Manual

### Design System
Based on **Light Spectrum** design tokens:
- **Primary:** Plum (#8B2682)
- **Secondary:** Eastern Blue (#2898A2)
- **Neutral:** Shark grays
- **Typography:** Inter with fluid sizing (clamp)

### Responsive Breakpoints
| Breakpoint | Width | Description |
|------------|-------|-------------|
| Mobile | < 640px | Phone portrait/landscape |
| Tablet | 640px - 1023px | Tablet, small laptop |
| Desktop | 1024px - 1199px | Standard desktop |
| Large Desktop | >= 1200px | Wide screens, sidebar visible |

### Multi-language Support
Uses `data-lang` attribute pattern:
```html
<span data-lang="en">English text</span>
<span data-lang="pt">Portuguese text</span>
```

---

## Reference Files Used

### Design Tokens (Source)
- `/Users/mohit/claude-workspace/projects/Lightmetrics/paper-setup/lightspectrum.tokens.json`
- `/Users/mohit/claude-workspace/projects/Lightmetrics/paper-setup/lightspectrum.css`

### HTML Structure Reference
- `/Users/mohit/claude-workspace/projects/Lightmetrics/installer 2.0/installer-web-guide/dist/installer-guide.html`

### Content Structure Reference
- `/Users/mohit/claude-workspace/projects/Lightmetrics/installer 2.0/03_final_pdf_content.md`

### Skill Structure Reference
- `/Users/mohit/.claude/skills/skill-creator/SKILL.md`

---

## Verification Status

- [x] Scripts compile successfully (`generate_html.py`, `validate_document.py`)
- [x] Test document generation works
- [x] Validation passes with proper structure
- [x] Language switching pattern implemented
- [x] Fluid typography with CSS clamp()
- [x] Mobile/tablet/desktop responsive breakpoints
- [x] Print styles included

---

## Usage

### Triggering the Skill
The skill triggers when users ask to:
- Create documentation
- Write a user guide
- Build an installation guide
- Generate technical specs
- Create process workflows
- Produce bilingual/multilingual documentation

### Example Prompts
- "Create an installation guide for our new device"
- "Generate a product specification document"
- "Help me write a technical manual in English and Portuguese"

---

## Files NOT Used (per plan)
- `/Users/mohit/claude-workspace/projects/Lightmetrics/brand-guidelines.md` — Excluded as specified

---

## Recent Changes

### Logo Path Fix (2026-04-03)
Updated all template and spec files to reference the correct logo asset:
- **Old:** `./assets/lightmetrics-logo.svg` (non-existent)
- **New:** `./assets/brand/brand_lightmetrics-logo.webp` (actual file)
- Files updated: all 4 templates + common-template-spec.md

### Sidebar Active States (2026-04-03)
Added scroll-based active state highlighting for sidebar navigation:
- **CSS:** `.sidebar__link.active` with left border accent, brand-colored number badge, semibold title (`base-styles.css`)
- **JS:** `IntersectionObserver` in `generate_scripts()` that tracks visible section and toggles `.active` class (`generate_html.py`)
- **Docs:** Active state behavior documented in `common-template-spec.md`

### Image Rules & Content Assembly (2026-04-04)
Comprehensive image extraction and referencing rules added to SKILL.md:
- 3 source types: Figma design URLs, FigJam board URLs, manual images
- Strict naming convention per document type (`s1_0-description.ext`, `ch1_0-description.ext`, etc.)
- Image manifest v2.0 schema with full source provenance
- MCP tool selection matrix for Figma/FigJam extraction
- Phase 1 Discovery made interactive with `AskUserQuestion` batches

### Content Drafting Phase & Usage Guide (2026-04-04)
- Workflow expanded from 7 to **8 phases** with new Phase 3: Content Drafting
- `final_content.md` is now written and approved before image assembly
- Language translations generated and approved in Phase 3 (`final_content_{lang}.md`)
- Entry-point menu added: "Create a document" or "How to use this skill"
- Full inline walkthrough guide added covering all 8 phases, document types, content collection, tips, and resuming sessions

---

## ~~Planned: How to Use This Skill Guide~~ ✅ Implemented (2026-04-04)

Implemented as the "Getting Started" entry-point menu and "How to Use This Skill" inline guide section in SKILL.md.

---

## Next Steps

1. **Test with real content** — Create actual installation guide using the full 8-phase workflow
2. **Figma integration test** — Verify screenshot extraction via MCP
3. **Evaluate and iterate** — Run skill-creator evals if needed
