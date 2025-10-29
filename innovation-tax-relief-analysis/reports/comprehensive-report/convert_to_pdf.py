#!/usr/bin/env python3
"""
Convert comprehensive report markdown files to PDF
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import re

# Order of files to include in PDF
FILE_ORDER = [
    "00-press-summary.md",
    "00-cover-and-toc.md",
    "01-executive-summary-PL.md",
    "02-executive-summary-EN.md",
    "03-chapter-1-introduction.md",
    "04-chapter-2-methodology.md",
    "05-chapter-3-ecosystem-analysis.md",
    "06-chapter-4-statistical-gap.md",
    "07-chapter-5-international-comparisons.md",
    "08-chapter-6-solutions-analysis.md",
    "09-chapter-7-implications-recommendations.md",
    "10-chapter-8-conclusions.md",
    "11-appendices.md",
]

# CSS styling for professional PDF
PDF_STYLES = """
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;

    @top-center {
        content: "Polski Ekosystem Ulg Podatkowych na Innowacje";
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 9pt;
        color: #666;
    }

    @bottom-center {
        content: "Strona " counter(page) " z " counter(pages);
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 9pt;
        color: #666;
    }
}

body {
    font-family: 'Segoe UI', 'Calibri', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
    text-align: justify;
}

h1 {
    font-size: 24pt;
    font-weight: bold;
    color: #1a1a1a;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
    page-break-after: avoid;
    border-bottom: 3px solid #0066cc;
    padding-bottom: 0.3em;
}

h2 {
    font-size: 18pt;
    font-weight: bold;
    color: #0066cc;
    margin-top: 1.2em;
    margin-bottom: 0.6em;
    page-break-after: avoid;
}

h3 {
    font-size: 14pt;
    font-weight: bold;
    color: #333;
    margin-top: 1em;
    margin-bottom: 0.5em;
    page-break-after: avoid;
}

h4 {
    font-size: 12pt;
    font-weight: bold;
    color: #555;
    margin-top: 0.8em;
    margin-bottom: 0.4em;
}

p {
    margin-bottom: 0.8em;
    text-align: justify;
}

strong {
    font-weight: bold;
    color: #1a1a1a;
}

em {
    font-style: italic;
}

ul, ol {
    margin-left: 1.5em;
    margin-bottom: 0.8em;
}

li {
    margin-bottom: 0.3em;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

th {
    background-color: #0066cc;
    color: white;
    font-weight: bold;
    padding: 8px;
    text-align: left;
    border: 1px solid #004499;
}

td {
    padding: 6px 8px;
    border: 1px solid #ddd;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

blockquote {
    margin: 1em 2em;
    padding: 0.5em 1em;
    background-color: #f0f8ff;
    border-left: 4px solid #0066cc;
    font-style: italic;
}

code {
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    background-color: #f4f4f4;
    padding: 2px 4px;
    border-radius: 3px;
}

pre {
    background-color: #f4f4f4;
    padding: 1em;
    border-radius: 5px;
    overflow-x: auto;
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    line-height: 1.4;
}

a {
    color: #0066cc;
    text-decoration: none;
}

.page-break {
    page-break-before: always;
}

/* Cover page styling */
.cover-page {
    text-align: center;
    padding-top: 3cm;
}

.cover-page h1 {
    font-size: 32pt;
    border-bottom: none;
    margin-bottom: 0.5em;
}

.cover-page h2 {
    font-size: 18pt;
    color: #666;
    margin-top: 0.5em;
}

/* Executive summary boxes */
.key-message {
    background-color: #e6f2ff;
    padding: 1em;
    border-left: 5px solid #0066cc;
    margin: 1em 0;
}

/* Emoji support */
.emoji {
    font-size: 1.2em;
}
"""

def process_markdown(content):
    """Process markdown content and convert to HTML"""
    # Convert markdown to HTML with extensions
    html = markdown.markdown(
        content,
        extensions=[
            'tables',
            'fenced_code',
            'nl2br',
            'sane_lists',
        ]
    )
    return html

def combine_markdown_files(file_list, base_dir):
    """Combine multiple markdown files into single HTML"""
    combined_html = []

    combined_html.append("""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>Polski Ekosystem Ulg Podatkowych na Innowacje</title>
    </head>
    <body>
    """)

    for i, filename in enumerate(file_list):
        filepath = base_dir / filename

        if not filepath.exists():
            print(f"Warning: File not found: {filename}")
            continue

        print(f"Processing: {filename}")

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add page break before each new file (except first)
        if i > 0:
            combined_html.append('<div class="page-break"></div>')

        # Convert markdown to HTML
        html_content = process_markdown(content)
        combined_html.append(html_content)

    combined_html.append("""
    </body>
    </html>
    """)

    return '\n'.join(combined_html)

def main():
    """Main conversion function"""
    base_dir = Path(__file__).parent
    output_pdf = base_dir / "Polski_Ekosystem_Ulg_Podatkowych_Raport.pdf"

    print("Starting PDF conversion...")
    print(f"Base directory: {base_dir}")

    # Combine all markdown files
    print("\nCombining markdown files...")
    html_content = combine_markdown_files(FILE_ORDER, base_dir)

    # Save HTML for debugging (optional)
    html_debug = base_dir / "debug_output.html"
    with open(html_debug, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Debug HTML saved to: {html_debug}")

    # Convert to PDF
    print("\nConverting to PDF...")
    try:
        HTML(string=html_content, base_url=str(base_dir)).write_pdf(
            output_pdf,
            stylesheets=[CSS(string=PDF_STYLES)]
        )
        print(f"\n✓ PDF successfully created: {output_pdf}")
        print(f"  File size: {output_pdf.stat().st_size / 1024 / 1024:.2f} MB")
    except Exception as e:
        print(f"\n✗ Error creating PDF: {e}")
        raise

    return output_pdf

if __name__ == "__main__":
    main()
