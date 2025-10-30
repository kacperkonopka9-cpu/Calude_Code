#!/usr/bin/env python3
"""
Convert comprehensive report markdown files to professional HTML
(Ready for Print-to-PDF via browser)
"""

import markdown
from pathlib import Path
import re

# Order of files to include
FILE_ORDER = [
    ("00-cover-and-toc.md", "Cover & Table of Contents"),
    ("01-executive-summary-PL.md", "Streszczenie Wykonawcze (Polski)"),
    ("02-executive-summary-EN.md", "Executive Summary (English)"),
    ("03-chapter-1-introduction.md", "Chapter 1: Introduction"),
    ("04-chapter-2-methodology.md", "Chapter 2: Methodology"),
    ("05-chapter-3-ecosystem-analysis.md", "Chapter 3: Ecosystem Analysis"),
    ("06-chapter-4-statistical-gap.md", "Chapter 4: Statistical Gap"),
    ("07-chapter-5-international-comparisons.md", "Chapter 5: International Comparisons"),
    ("08-chapter-6-solutions-analysis.md", "Chapter 6: Solutions Analysis"),
    ("09-chapter-7-implications-recommendations.md", "Chapter 7: Implications & Recommendations"),
    ("10-chapter-8-conclusions.md", "Chapter 8: Conclusions"),
    ("11-appendices.md", "Appendices"),
    ("00-press-summary.md", "Press Summary"),
]

# Professional HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Polski Ekosystem Ulg Podatkowych na Innowacje - Raport 2017-2024</title>
    <style>
        /* Print-optimized styles */
        @page {
            size: A4;
            margin: 2cm;
        }

        @media print {
            body {
                font-size: 10pt;
            }

            .no-print {
                display: none;
            }

            .page-break {
                page-break-before: always;
            }

            h1, h2, h3 {
                page-break-after: avoid;
            }

            table, figure {
                page-break-inside: avoid;
            }
        }

        /* General styles */
        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Calibri', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.7;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }

        .container {
            background: white;
            padding: 40px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }

        /* Typography */
        h1 {
            font-size: 28pt;
            font-weight: bold;
            color: #1a1a1a;
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            border-bottom: 3px solid #0066cc;
            padding-bottom: 0.3em;
        }

        h1:first-child {
            margin-top: 0;
        }

        h2 {
            font-size: 20pt;
            font-weight: bold;
            color: #0066cc;
            margin-top: 1.5em;
            margin-bottom: 0.6em;
        }

        h3 {
            font-size: 15pt;
            font-weight: bold;
            color: #333;
            margin-top: 1.2em;
            margin-bottom: 0.5em;
        }

        h4 {
            font-size: 13pt;
            font-weight: bold;
            color: #555;
            margin-top: 1em;
            margin-bottom: 0.4em;
        }

        p {
            margin-bottom: 1em;
            text-align: justify;
        }

        strong {
            font-weight: 700;
            color: #1a1a1a;
        }

        em {
            font-style: italic;
        }

        /* Lists */
        ul, ol {
            margin-left: 2em;
            margin-bottom: 1em;
        }

        li {
            margin-bottom: 0.4em;
        }

        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
            font-size: 10pt;
        }

        th {
            background-color: #0066cc;
            color: white;
            font-weight: bold;
            padding: 10px;
            text-align: left;
            border: 1px solid #004499;
        }

        td {
            padding: 8px 10px;
            border: 1px solid #ddd;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        tr:hover {
            background-color: #f0f8ff;
        }

        /* Blockquotes */
        blockquote {
            margin: 1.5em 2em;
            padding: 1em;
            background-color: #f0f8ff;
            border-left: 5px solid #0066cc;
            font-style: italic;
        }

        /* Code */
        code {
            font-family: 'Courier New', 'Consolas', monospace;
            font-size: 9pt;
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            color: #c7254e;
        }

        pre {
            background-color: #f4f4f4;
            padding: 1.2em;
            border-radius: 5px;
            overflow-x: auto;
            border: 1px solid #ddd;
        }

        pre code {
            background: none;
            padding: 0;
            color: inherit;
        }

        /* Links */
        a {
            color: #0066cc;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Horizontal rule */
        hr {
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 2em 0;
        }

        /* Special boxes */
        .info-box {
            background-color: #e6f2ff;
            padding: 1.2em;
            border-left: 5px solid #0066cc;
            margin: 1.5em 0;
        }

        .warning-box {
            background-color: #fff3cd;
            padding: 1.2em;
            border-left: 5px solid #ff9800;
            margin: 1.5em 0;
        }

        .success-box {
            background-color: #d4edda;
            padding: 1.2em;
            border-left: 5px solid #28a745;
            margin: 1.5em 0;
        }

        /* Navigation (no-print) */
        .navigation {
            position: sticky;
            top: 0;
            background: #0066cc;
            color: white;
            padding: 15px;
            margin: -40px -40px 30px -40px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            z-index: 1000;
        }

        .navigation h3 {
            margin: 0 0 10px 0;
            color: white;
            font-size: 14pt;
        }

        .navigation button {
            background: white;
            color: #0066cc;
            border: none;
            padding: 10px 20px;
            margin-right: 10px;
            cursor: pointer;
            border-radius: 5px;
            font-weight: bold;
        }

        .navigation button:hover {
            background: #f0f8ff;
        }

        /* Chapter markers */
        .chapter-marker {
            color: #0066cc;
            font-weight: bold;
            margin-top: 3em;
            padding-top: 1em;
            border-top: 3px solid #0066cc;
        }

        /* Footer */
        .report-footer {
            margin-top: 3em;
            padding-top: 2em;
            border-top: 2px solid #e0e0e0;
            text-align: center;
            color: #666;
            font-size: 9pt;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="navigation no-print">
            <h3>📊 Polski Ekosystem Ulg Podatkowych na Innowacje</h3>
            <button onclick="window.print()">🖨️ Print to PDF (Ctrl+P)</button>
            <button onclick="document.body.style.zoom='100%'">🔍 Reset Zoom</button>
            <button onclick="document.body.style.zoom=(parseFloat(document.body.style.zoom||1)+0.1)*100+'%'">🔍+ Zoom In</button>
            <button onclick="document.body.style.zoom=(parseFloat(document.body.style.zoom||1)-0.1)*100+'%'">🔍- Zoom Out</button>
        </div>

{CONTENT}

        <div class="report-footer">
            <p><strong>Polski Ekosystem Ulg Podatkowych na Innowacje</strong></p>
            <p>Analiza Danych 2017-2024 i Luka Raportowania Statystycznego</p>
            <p>Wersja 1.0 | Październik 2025</p>
            <p>Licencja: Creative Commons Attribution 4.0 International (CC BY 4.0)</p>
        </div>
    </div>

    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Print instructions
        console.log('%c📊 To convert this report to PDF:', 'font-size: 16px; font-weight: bold; color: #0066cc;');
        console.log('%c1. Press Ctrl+P (or Cmd+P on Mac)', 'font-size: 14px;');
        console.log('%c2. Select "Save as PDF" as printer', 'font-size: 14px;');
        console.log('%c3. Adjust settings: Margins (Default), Background graphics (enabled)', 'font-size: 14px;');
        console.log('%c4. Click "Save"', 'font-size: 14px;');
    </script>
</body>
</html>
"""

def process_markdown(content):
    """Process markdown content and convert to HTML"""
    html = markdown.markdown(
        content,
        extensions=[
            'tables',
            'fenced_code',
            'nl2br',
            'sane_lists',
            'codehilite',
        ]
    )
    return html

def main():
    """Main conversion function"""
    base_dir = Path(__file__).parent
    output_html = base_dir / "Polski_Ekosystem_Ulg_Podatkowych_Raport.html"

    print("Starting HTML conversion...")
    print(f"Base directory: {base_dir}")

    # Combine all markdown files
    combined_content = []

    for i, (filename, title) in enumerate(FILE_ORDER):
        filepath = base_dir / filename

        if not filepath.exists():
            print(f"Warning: File not found: {filename}")
            continue

        print(f"Processing: {filename}")

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add page break and chapter marker before each new file (except first)
        if i > 0:
            combined_content.append('<div class="page-break"></div>')
            combined_content.append(f'<div class="chapter-marker">📄 {title}</div>')

        # Convert markdown to HTML
        html_content = process_markdown(content)
        combined_content.append(html_content)

    # Combine all content
    final_content = '\n\n'.join(combined_content)

    # Create final HTML
    final_html = HTML_TEMPLATE.replace('{CONTENT}', final_content)

    # Save HTML
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"\nHTML successfully created: {output_html}")
    print(f"File size: {output_html.stat().st_size / 1024 / 1024:.2f} MB")
    print("\n" + "="*60)
    print("TO CONVERT TO PDF:")
    print("="*60)
    print("1. Open the HTML file in your browser (Chrome, Edge, Firefox)")
    print("2. Press Ctrl+P (or Cmd+P on Mac)")
    print("3. Select 'Save as PDF' as printer")
    print("4. Settings:")
    print("   - Margins: Default")
    print("   - Background graphics: ✓ Enabled")
    print("   - Headers and footers: Optional")
    print("5. Click 'Save'")
    print("="*60)

    return output_html

if __name__ == "__main__":
    main()
