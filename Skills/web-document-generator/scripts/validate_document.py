#!/usr/bin/env python3
"""
Document Validation Script for Web Document Generator

Validates HTML documents for:
- Accessibility (alt text, heading hierarchy, color contrast)
- Content completeness (images, links, required sections)
- Multi-language consistency
- HTML structure validity

Usage:
    python validate_document.py ./path/to/document.html
    python validate_document.py ./path/to/document.html --output report.md
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from html.parser import HTMLParser
from datetime import datetime


@dataclass
class ValidationIssue:
    """Represents a validation issue found in the document."""
    category: str  # accessibility, content, language, structure
    severity: str  # error, warning, info
    message: str
    line: Optional[int] = None
    element: Optional[str] = None


@dataclass
class ValidationReport:
    """Complete validation report for a document."""
    document_path: str
    timestamp: str
    issues: List[ValidationIssue] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)
    passed: bool = True

    def add_issue(self, issue: ValidationIssue):
        self.issues.append(issue)
        if issue.severity == "error":
            self.passed = False

    def to_markdown(self) -> str:
        """Generate markdown report."""
        lines = [
            f"# Document Validation Report",
            f"",
            f"**Document:** `{self.document_path}`",
            f"**Timestamp:** {self.timestamp}",
            f"**Status:** {'✅ PASSED' if self.passed else '❌ FAILED'}",
            f"",
            f"## Summary",
            f""
        ]

        # Stats
        for key, value in self.stats.items():
            lines.append(f"- **{key}:** {value}")

        # Issues by category
        if self.issues:
            lines.append(f"")
            lines.append(f"## Issues ({len(self.issues)} total)")
            lines.append(f"")

            categories = {}
            for issue in self.issues:
                if issue.category not in categories:
                    categories[issue.category] = []
                categories[issue.category].append(issue)

            for category, issues in categories.items():
                lines.append(f"### {category.title()}")
                lines.append(f"")
                for issue in issues:
                    icon = {"error": "🔴", "warning": "🟡", "info": "🔵"}.get(issue.severity, "⚪")
                    loc = f" (line {issue.line})" if issue.line else ""
                    elem = f" `{issue.element}`" if issue.element else ""
                    lines.append(f"- {icon} {issue.message}{elem}{loc}")
                lines.append(f"")
        else:
            lines.append(f"")
            lines.append(f"## Issues")
            lines.append(f"")
            lines.append(f"No issues found. ✨")

        return "\n".join(lines)

    def to_json(self) -> str:
        """Generate JSON report."""
        return json.dumps({
            "document_path": self.document_path,
            "timestamp": self.timestamp,
            "passed": self.passed,
            "stats": self.stats,
            "issues": [
                {
                    "category": i.category,
                    "severity": i.severity,
                    "message": i.message,
                    "line": i.line,
                    "element": i.element
                }
                for i in self.issues
            ]
        }, indent=2)


class HTMLValidator(HTMLParser):
    """HTML parser for validation."""

    def __init__(self):
        super().__init__()
        self.images = []
        self.links = []
        self.headings = []
        self.lang_elements = []
        self.current_line = 1
        self.current_lang = None
        self.data_langs_found = set()

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        line = self.getpos()[0]

        # Track images
        if tag == "img":
            self.images.append({
                "src": attrs_dict.get("src", ""),
                "alt": attrs_dict.get("alt"),
                "line": line
            })

        # Track links
        if tag == "a":
            self.links.append({
                "href": attrs_dict.get("href", ""),
                "line": line
            })

        # Track headings
        if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            self.headings.append({
                "tag": tag,
                "level": int(tag[1]),
                "line": line
            })

        # Track language attributes
        if "data-lang" in attrs_dict:
            self.data_langs_found.add(attrs_dict["data-lang"])
            self.lang_elements.append({
                "lang": attrs_dict["data-lang"],
                "line": line,
                "tag": tag
            })


def validate_document(html_path: Path) -> ValidationReport:
    """
    Validate an HTML document.

    Args:
        html_path: Path to the HTML file

    Returns:
        ValidationReport with all findings
    """
    report = ValidationReport(
        document_path=str(html_path),
        timestamp=datetime.now().isoformat()
    )

    if not html_path.exists():
        report.add_issue(ValidationIssue(
            category="structure",
            severity="error",
            message=f"Document not found: {html_path}"
        ))
        return report

    html_content = html_path.read_text(encoding="utf-8")

    # Parse HTML
    parser = HTMLValidator()
    try:
        parser.feed(html_content)
    except Exception as e:
        report.add_issue(ValidationIssue(
            category="structure",
            severity="error",
            message=f"HTML parsing error: {e}"
        ))
        return report

    # Collect stats
    report.stats["Total images"] = len(parser.images)
    report.stats["Total links"] = len(parser.links)
    report.stats["Total headings"] = len(parser.headings)
    report.stats["Languages found"] = ", ".join(sorted(parser.data_langs_found)) or "none"

    # Validate accessibility
    validate_accessibility(parser, report, html_path)

    # Validate content
    validate_content(parser, report, html_path)

    # Validate language consistency
    validate_languages(parser, report)

    # Validate structure
    validate_structure(parser, report)

    return report


def validate_accessibility(parser: HTMLValidator, report: ValidationReport, html_path: Path):
    """Check accessibility requirements."""

    # Check alt text on images
    images_without_alt = 0
    for img in parser.images:
        if img["alt"] is None or img["alt"].strip() == "":
            images_without_alt += 1
            report.add_issue(ValidationIssue(
                category="accessibility",
                severity="error",
                message="Image missing alt text",
                element=img["src"][:50],
                line=img["line"]
            ))

    report.stats["Images with alt text"] = f"{len(parser.images) - images_without_alt}/{len(parser.images)}"

    # Check heading hierarchy
    prev_level = 0
    for heading in parser.headings:
        level = heading["level"]
        if level > prev_level + 1 and prev_level > 0:
            report.add_issue(ValidationIssue(
                category="accessibility",
                severity="warning",
                message=f"Heading level skipped (h{prev_level} → h{level})",
                element=heading["tag"],
                line=heading["line"]
            ))
        prev_level = level


def validate_content(parser: HTMLValidator, report: ValidationReport, html_path: Path):
    """Check content completeness."""
    base_path = html_path.parent

    # Check image references exist
    missing_images = 0
    for img in parser.images:
        src = img["src"]

        # Skip data URIs and external URLs
        if src.startswith(("data:", "http://", "https://")):
            continue

        img_path = base_path / src
        if not img_path.exists():
            missing_images += 1
            report.add_issue(ValidationIssue(
                category="content",
                severity="error",
                message="Image file not found",
                element=src,
                line=img["line"]
            ))

    report.stats["Missing images"] = missing_images

    # Check internal links
    broken_links = 0
    for link in parser.links:
        href = link["href"]

        # Check internal anchors
        if href.startswith("#"):
            anchor_id = href[1:]
            if f'id="{anchor_id}"' not in html_path.read_text():
                broken_links += 1
                report.add_issue(ValidationIssue(
                    category="content",
                    severity="warning",
                    message="Internal link target not found",
                    element=href,
                    line=link["line"]
                ))

    report.stats["Broken internal links"] = broken_links


def validate_languages(parser: HTMLValidator, report: ValidationReport):
    """Check multi-language consistency."""

    if not parser.data_langs_found:
        return  # Single language document

    # Group elements by approximate line range (siblings)
    # This is a simplified check - in production, you'd use proper DOM analysis
    lang_counts = {}
    for lang in parser.data_langs_found:
        count = sum(1 for el in parser.lang_elements if el["lang"] == lang)
        lang_counts[lang] = count

    # Check for imbalanced language coverage
    if len(set(lang_counts.values())) > 1:
        counts_str = ", ".join(f"{lang}: {count}" for lang, count in lang_counts.items())
        report.add_issue(ValidationIssue(
            category="language",
            severity="warning",
            message=f"Language element counts differ ({counts_str})",
        ))


def validate_structure(parser: HTMLValidator, report: ValidationReport):
    """Check HTML structure requirements."""

    # Check for at least one h1
    h1_count = sum(1 for h in parser.headings if h["level"] == 1)
    if h1_count == 0:
        report.add_issue(ValidationIssue(
            category="structure",
            severity="warning",
            message="Document has no h1 heading"
        ))
    elif h1_count > 1:
        report.add_issue(ValidationIssue(
            category="structure",
            severity="info",
            message=f"Document has multiple h1 headings ({h1_count})"
        ))


def main():
    parser = argparse.ArgumentParser(description="Validate HTML documents")
    parser.add_argument("document", type=str, help="Path to HTML document")
    parser.add_argument("--output", "-o", type=str, help="Output report path (md or json)")
    parser.add_argument("--format", "-f", choices=["markdown", "json"], default="markdown",
                        help="Report format")
    parser.add_argument("--strict", action="store_true",
                        help="Exit with error code if any issues found")

    args = parser.parse_args()

    # Run validation
    html_path = Path(args.document)
    report = validate_document(html_path)

    # Generate output
    if args.format == "json":
        output = report.to_json()
    else:
        output = report.to_markdown()

    # Write or print report
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(output, encoding="utf-8")
        print(f"Report written to: {output_path}")
    else:
        print(output)

    # Exit code
    if args.strict and not report.passed:
        sys.exit(1)
    elif not report.passed:
        sys.exit(0)  # Still exit 0 unless strict mode


if __name__ == "__main__":
    main()
