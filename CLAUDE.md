# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repo contains custom Claude Code skills for Lightmetrics. Skills are installable prompt-driven workflows that extend Claude Code's capabilities.

## Repository Structure

- `Skills/` — Contains all installable skills, each in its own subdirectory
- `Skills/web-document-generator/` — The primary skill: generates professional B2B technical documents as self-contained HTML files

### Web Document Generator Skill

A 7-phase workflow (Discovery → Structure → Content Assembly → Draft → Review → Output → Delivery) that produces self-contained HTML documents with multi-language support.

Key paths within `Skills/web-document-generator/`:
- `SKILL.md` — Skill definition and full workflow specification
- `references/design-tokens.md` — LightSpectrum design system tokens (sourced from `projects/Lightmetrics/paper-setup/lightspectrum.css`)
- `references/templates/` — Document type templates (installation-guide, product-spec, process-workflow, technical-manual)
- `references/writing-guidelines.md` — Content style guide
- `assets/base-styles.css` — Embedded LightSpectrum CSS for all documents
- `scripts/validate_document.py` — HTML validation (accessibility, links, images, multi-language consistency)
- `scripts/generate_html.py` — HTML generation utilities

## Common Commands

```bash
# Validate a generated document
python Skills/web-document-generator/scripts/validate_document.py ./path/to/document.html
python Skills/web-document-generator/scripts/validate_document.py ./path/to/document.html --output report.md

# Generate HTML from a template
python Skills/web-document-generator/scripts/generate_html.py --template installation-guide --output ./output/guide.html
python Skills/web-document-generator/scripts/generate_html.py --structure ./project/structure.md --output ./output/doc.html
```

## Key Design Decisions

- **Self-contained HTML**: All generated documents embed CSS inline via `<style>` tags. Images use relative `./assets/` paths or base64 encoding for single-file output.
- **Multi-language**: Uses `data-lang` attributes (e.g., `<span data-lang="en">`) with a language selector UI, not separate files per language.
- **Design system**: All styling follows the LightSpectrum design system. Token updates must be synced from the authoritative source.
- **Responsive breakpoints**: Mobile (<640px), Tablet (640-1199px), Desktop (>=1200px). Mobile-first approach.
