#!/usr/bin/env python3
"""
HTML Generation Utilities for Web Document Generator

This script provides utilities for generating self-contained HTML documents
using the Light Spectrum design system.

Usage:
    python generate_html.py --template installation-guide --output ./output/guide.html
    python generate_html.py --structure ./project/structure.md --output ./output/doc.html
"""

import argparse
import json
import os
import re
import base64
from pathlib import Path
from typing import Optional, Dict, List, Any
from datetime import datetime


# Base HTML template
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <style>
{styles}
  </style>
</head>
<body id="top" data-lang="{default_lang}">
{header}
  <div class="app-layout">
{sidebar}
    <main class="app-content">
{hero}
{content}
    </main>
  </div>
{scripts}
</body>
</html>
'''


def load_base_styles(skill_path: Optional[Path] = None) -> str:
    """Load base CSS styles from assets."""
    if skill_path is None:
        skill_path = Path(__file__).parent.parent

    css_path = skill_path / "assets" / "base-styles.css"
    if css_path.exists():
        return css_path.read_text()

    # Return minimal fallback styles
    return '''
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', system-ui, sans-serif; background: #F8FAFC; color: #18181B; line-height: 1.6; }
'''


def generate_header(
    brand_name: str = "Document",
    brand_sub: str = "",
    languages: List[str] = None,
    logo_path: Optional[str] = None
) -> str:
    """Generate the site header HTML."""
    languages = languages or ["en"]

    # Language options
    lang_options = ""
    lang_names = {"en": "English", "pt": "Português", "es": "Español"}
    for lang in languages:
        name = lang_names.get(lang, lang.upper())
        lang_options += f'        <option value="{lang}">{name}</option>\n'

    logo_html = ""
    if logo_path:
        logo_html = f'<img src="{logo_path}" alt="{brand_name}" class="brand-logo-img" />'

    return f'''
  <header class="site-header">
    <a href="#top" class="site-header__brand">
      {logo_html}
      <span class="brand-divider"></span>
      <div class="brand-text">
        <span class="brand-name">{brand_name}</span>
        <span class="brand-sub">{brand_sub}</span>
      </div>
    </a>
    <div class="lang-selector">
      <select id="langSelect" class="lang-selector__dropdown" onchange="setLanguage(this.value)" aria-label="Select language">
{lang_options}      </select>
    </div>
    <button class="hamburger" onclick="openSidebar()" aria-label="Open navigation">
      <span></span><span></span><span></span>
    </button>
  </header>
'''


def generate_sidebar(steps: List[Dict[str, Any]], languages: List[str] = None) -> str:
    """Generate the sidebar navigation HTML."""
    languages = languages or ["en"]

    items = ""
    for i, step in enumerate(steps, 1):
        step_id = step.get("id", f"step-{i}")

        # Generate multi-language titles
        titles = ""
        subtitles = ""
        for lang in languages:
            title = step.get(f"title_{lang}", step.get("title", f"Step {i}"))
            subtitle = step.get(f"subtitle_{lang}", step.get("subtitle", ""))
            titles += f'<span data-lang="{lang}">{title}</span>'
            if subtitle:
                subtitles += f'<span data-lang="{lang}">{subtitle}</span>'

        items += f'''
    <li class="sidebar__item">
      <a href="#{step_id}" class="sidebar__link" onclick="closeSidebar()">
        <span class="sidebar__num">{i}</span>
        <span class="sidebar__text">
          <span class="sidebar__step-title">{titles}</span>
          <span class="sidebar__subtitle">{subtitles}</span>
        </span>
      </a>
    </li>'''

    return f'''
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>
    <nav class="sidebar" id="sidebar">
      <div class="sidebar__head">
        <span>
          <span data-lang="en">Navigation</span>
          <span data-lang="pt">Navegação</span>
          <span data-lang="es">Navegación</span>
        </span>
        <button onclick="closeSidebar()" class="sidebar__close">✕</button>
      </div>
      <ol class="sidebar__list">{items}
      </ol>
      <div class="sidebar__foot">
        <a href="#top" onclick="closeSidebar()">
          <span data-lang="en">↑ Back to top</span>
          <span data-lang="pt">↑ Voltar ao topo</span>
          <span data-lang="es">↑ Volver arriba</span>
        </a>
      </div>
    </nav>
'''


def generate_hero(
    eyebrow: str = "",
    title: Dict[str, str] = None,
    description: Dict[str, str] = None,
    chips: List[str] = None
) -> str:
    """Generate the page hero section."""
    title = title or {"en": "Document Title"}
    description = description or {}
    chips = chips or []

    title_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in title.items())
    desc_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in description.items())
    chips_html = "".join(f'<span class="page-hero__chip">{chip}</span>' for chip in chips)

    return f'''
  <div class="page-hero">
    <p class="page-hero__eyebrow">{eyebrow}</p>
    <h1 class="page-hero__title">{title_html}</h1>
    <p class="page-hero__desc">{desc_html}</p>
    <div class="page-hero__chips">{chips_html}</div>
  </div>
'''


def generate_step_section(
    step_num: int,
    total_steps: int,
    step_id: str,
    title: Dict[str, str],
    purpose: Dict[str, str],
    substeps: List[Dict[str, Any]],
    is_conditional: bool = False
) -> str:
    """Generate a step section with substeps."""
    title_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in title.items())
    purpose_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in purpose.items())

    conditional_badge = ""
    if is_conditional:
        conditional_badge = '<span class="step-section__conditional">Conditional</span>'

    substeps_html = ""
    for substep in substeps:
        substeps_html += generate_substep(substep)

    return f'''
    <section class="step-section" id="{step_id}">
      <div class="step-section__header">
        <div class="step-section__meta">
          <span class="step-section__badge">
            <span data-lang="en">Step {step_num}</span>
            <span data-lang="pt">Passo {step_num}</span>
            <span data-lang="es">Paso {step_num}</span>
          </span>
          {conditional_badge}
        </div>
        <h2 class="step-section__title">{title_html}</h2>
        <p class="step-section__indicator">
          <span data-lang="en">STEP {step_num:02d}/{total_steps:02d}</span>
          <span data-lang="pt">PASSO {step_num:02d}/{total_steps:02d}</span>
          <span data-lang="es">PASO {step_num:02d}/{total_steps:02d}</span>
        </p>
        <p class="step-section__purpose">{purpose_html}</p>
      </div>
      <div class="step-section__substeps">
        {substeps_html}
      </div>
    </section>
'''


def generate_substep(substep: Dict[str, Any]) -> str:
    """Generate a substep card."""
    badge = substep.get("badge", "1.1")
    title = substep.get("title", {"en": "Sub-step"})
    instructions = substep.get("instructions", [])
    screenshot = substep.get("screenshot")

    title_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in title.items())

    instructions_html = ""
    for instruction in instructions:
        if isinstance(instruction, dict):
            instr_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in instruction.items())
        else:
            instr_html = instruction
        instructions_html += f"<li>{instr_html}</li>"

    screenshot_html = ""
    if screenshot:
        src = screenshot.get("src", "")
        alt = screenshot.get("alt", "Screenshot")
        caption = screenshot.get("caption", "")
        screenshot_html = f'''
        <div class="screenshot-panel">
          <img
            src="{src}"
            alt="{alt}"
            class="screenshot-panel__img"
            loading="lazy"
            onclick="this.classList.toggle('screenshot-panel__img--zoom')"
          />
          <p class="screenshot-panel__caption">{caption}</p>
        </div>'''

    inner_class = "substep__inner--with-screenshot" if screenshot else ""

    return f'''
    <div class="substep">
      <div class="substep__inner {inner_class}">
        <div class="substep__content">
          <div class="substep__header">
            <span class="substep__badge">{badge}</span>
            <h3 class="substep__title">{title_html}</h3>
          </div>
          <ol class="substep__instructions">
            {instructions_html}
          </ol>
        </div>
        {screenshot_html}
      </div>
    </div>
'''


def generate_callout(callout_type: str, content: Dict[str, str], icon: str = None) -> str:
    """Generate a callout box."""
    icons = {
        "warning": "⚠️",
        "info": "ℹ️",
        "conditional": "🔀",
        "success": "✅"
    }
    icon = icon or icons.get(callout_type, "📌")

    content_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in content.items())

    return f'''
    <div class="callout callout--{callout_type}">
      <span class="callout__icon">{icon}</span>
      <div class="callout__body">{content_html}</div>
    </div>
'''


def generate_decision_table(
    title: Dict[str, str],
    headers: List[Dict[str, str]],
    rows: List[List[Dict[str, str]]]
) -> str:
    """Generate a decision table."""
    title_html = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in title.items())

    headers_html = ""
    for header in headers:
        header_text = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in header.items())
        headers_html += f"<th>{header_text}</th>"

    rows_html = ""
    for row in rows:
        row_cells = ""
        for cell in row:
            if isinstance(cell, dict):
                cell_text = "".join(f'<span data-lang="{lang}">{text}</span>' for lang, text in cell.items())
            else:
                cell_text = str(cell)
            row_cells += f"<td>{cell_text}</td>"
        rows_html += f"<tr>{row_cells}</tr>"

    return f'''
    <details class="decision-table">
      <summary class="decision-table__toggle">{title_html}</summary>
      <div class="decision-table__wrap">
        <table class="decision-table__table">
          <thead><tr>{headers_html}</tr></thead>
          <tbody>{rows_html}</tbody>
        </table>
      </div>
    </details>
'''


def generate_scripts(languages: List[str] = None) -> str:
    """Generate JavaScript for interactivity."""
    languages = languages or ["en"]
    default_lang = languages[0]

    return f'''
  <script>
    // Language switching
    function setLanguage(lang) {{
      document.body.setAttribute('data-lang', lang);
      localStorage.setItem('doc-lang', lang);
    }}

    // Load saved language preference
    const savedLang = localStorage.getItem('doc-lang');
    if (savedLang) {{
      document.body.setAttribute('data-lang', savedLang);
      document.getElementById('langSelect').value = savedLang;
    }}

    // Sidebar controls
    function openSidebar() {{
      document.getElementById('sidebar').classList.add('open');
      document.getElementById('sidebarOverlay').classList.add('active');
      document.querySelector('.hamburger').classList.add('open');
    }}

    function closeSidebar() {{
      document.getElementById('sidebar').classList.remove('open');
      document.getElementById('sidebarOverlay').classList.remove('active');
      document.querySelector('.hamburger').classList.remove('open');
    }}

    // Close sidebar on escape key
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeSidebar();
    }});
  </script>
'''


def generate_document(config: Dict[str, Any], output_path: Optional[Path] = None) -> str:
    """
    Generate a complete HTML document from configuration.

    Args:
        config: Document configuration dictionary
        output_path: Optional path to write the output

    Returns:
        Generated HTML string
    """
    languages = config.get("languages", ["en"])
    default_lang = languages[0]

    # Load styles
    skill_path = config.get("skill_path")
    styles = load_base_styles(Path(skill_path) if skill_path else None)

    # Generate components
    header = generate_header(
        brand_name=config.get("brand_name", "Document"),
        brand_sub=config.get("brand_sub", ""),
        languages=languages,
        logo_path=config.get("logo_path")
    )

    steps = config.get("steps", [])
    sidebar = generate_sidebar(steps, languages) if steps else ""

    hero = generate_hero(
        eyebrow=config.get("eyebrow", ""),
        title=config.get("title", {"en": "Document"}),
        description=config.get("description", {}),
        chips=config.get("chips", [])
    )

    # Generate content sections
    content = ""
    total_steps = len(steps)
    for i, step in enumerate(steps, 1):
        content += generate_step_section(
            step_num=i,
            total_steps=total_steps,
            step_id=step.get("id", f"step-{i}"),
            title=step.get("title", {"en": f"Step {i}"}),
            purpose=step.get("purpose", {}),
            substeps=step.get("substeps", []),
            is_conditional=step.get("conditional", False)
        )

    scripts = generate_scripts(languages)

    # Assemble document
    html = HTML_TEMPLATE.format(
        title=config.get("document_title", "Document"),
        styles=styles,
        default_lang=default_lang,
        header=header,
        sidebar=sidebar,
        hero=hero,
        content=content,
        scripts=scripts
    )

    # Write output if path provided
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding="utf-8")
        print(f"Document generated: {output_path}")

    return html


def embed_images_as_base64(html: str, base_path: Path) -> str:
    """Convert image references to base64 embedded data URIs."""
    img_pattern = re.compile(r'src="([^"]+\.(png|jpg|jpeg|gif|webp|svg))"', re.IGNORECASE)

    def replace_with_base64(match):
        src = match.group(1)
        ext = match.group(2).lower()

        # Skip already embedded or external URLs
        if src.startswith(('data:', 'http://', 'https://')):
            return match.group(0)

        img_path = base_path / src
        if not img_path.exists():
            print(f"Warning: Image not found: {img_path}")
            return match.group(0)

        mime_types = {
            'png': 'image/png',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'gif': 'image/gif',
            'webp': 'image/webp',
            'svg': 'image/svg+xml'
        }
        mime_type = mime_types.get(ext, 'application/octet-stream')

        with open(img_path, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')

        return f'src="data:{mime_type};base64,{data}"'

    return img_pattern.sub(replace_with_base64, html)


def main():
    parser = argparse.ArgumentParser(description="Generate HTML documents")
    parser.add_argument("--config", type=str, help="Path to JSON config file")
    parser.add_argument("--output", type=str, required=True, help="Output HTML file path")
    parser.add_argument("--embed-images", action="store_true", help="Embed images as base64")
    parser.add_argument("--base-path", type=str, help="Base path for resolving relative images")

    args = parser.parse_args()

    # Load configuration
    if args.config:
        with open(args.config) as f:
            config = json.load(f)
    else:
        # Example configuration for testing
        config = {
            "document_title": "Test Document",
            "brand_name": "Test",
            "languages": ["en"],
            "title": {"en": "Test Document"},
            "steps": []
        }

    # Generate document
    html = generate_document(config, Path(args.output))

    # Optionally embed images
    if args.embed_images:
        base_path = Path(args.base_path) if args.base_path else Path(args.output).parent
        html = embed_images_as_base64(html, base_path)
        Path(args.output).write_text(html, encoding="utf-8")
        print("Images embedded as base64")


if __name__ == "__main__":
    main()
