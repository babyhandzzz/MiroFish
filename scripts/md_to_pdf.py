"""Convert MiroFish markdown report to styled PDF using pandoc + weasyprint."""

import subprocess
import sys
import os

REPORT_MD = sys.argv[1] if len(sys.argv) > 1 else "backend/uploads/reports/oil_shock_florida_tourism_report.md"
OUTPUT_PDF = sys.argv[2] if len(sys.argv) > 2 else REPORT_MD.replace('.md', '.pdf')

CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;
    @top-center {
        content: "MiroFish Simulation Report";
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #999;
    }
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #999;
    }
}

@page :first {
    @top-center { content: none; }
}

body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #1a1a1a;
    max-width: 100%;
}

h1 {
    font-size: 26pt;
    font-weight: 700;
    color: #0d2137;
    border-bottom: 3px solid #1a73e8;
    padding-bottom: 12px;
    margin-top: 40px;
    margin-bottom: 8px;
}

h1::after {
    content: "MiroFish AI Simulation Platform";
    display: block;
    font-size: 11pt;
    font-weight: 400;
    color: #5f6368;
    margin-top: 6px;
    letter-spacing: 0.5px;
}

h2 {
    font-size: 16pt;
    font-weight: 600;
    color: #1a73e8;
    margin-top: 32px;
    margin-bottom: 10px;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 6px;
    page-break-after: avoid;
}

h3 {
    font-size: 12pt;
    font-weight: 600;
    color: #0d2137;
    margin-top: 20px;
    margin-bottom: 6px;
}

p {
    margin-bottom: 10px;
    text-align: justify;
    orphans: 3;
    widows: 3;
}

blockquote {
    border-left: 4px solid #1a73e8;
    background: #f0f4ff;
    padding: 10px 16px;
    margin: 16px 0;
    font-style: italic;
    font-size: 9.5pt;
    color: #333;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
}

blockquote p {
    margin: 4px 0;
    text-align: left;
}

strong {
    color: #0d2137;
}

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 20px 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

th {
    background: #1a73e8;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
}

td {
    padding: 6px 10px;
    border-bottom: 1px solid #e0e0e0;
}

tr:nth-child(even) td {
    background: #f8f9fa;
}

ul, ol {
    margin-bottom: 10px;
    padding-left: 24px;
}

li {
    margin-bottom: 4px;
}

/* Cover page metadata block */
h1 + blockquote {
    border-left: none;
    background: #f8f9fa;
    text-align: center;
    font-style: normal;
    font-size: 11pt;
    color: #5f6368;
    border-radius: 4px;
    padding: 16px;
}
"""

# Step 1: Convert markdown to HTML via pandoc
html_tmp = OUTPUT_PDF.replace('.pdf', '.html')
print(f"Converting {REPORT_MD} -> HTML...")
result = subprocess.run(
    ["pandoc", REPORT_MD, "-f", "markdown", "-t", "html5", "--standalone",
     "--metadata", "title=MiroFish Simulation Report"],
    capture_output=True, text=True
)
if result.returncode != 0:
    print(f"Pandoc error: {result.stderr}")
    sys.exit(1)

html_content = result.stdout

# Inject CSS into the HTML
html_content = html_content.replace("</head>", f"<style>{CSS}</style></head>")

with open(html_tmp, 'w') as f:
    f.write(html_content)

# Step 2: Convert HTML to PDF via weasyprint
print(f"Converting HTML -> PDF ({OUTPUT_PDF})...")
from weasyprint import HTML
HTML(filename=html_tmp).write_pdf(OUTPUT_PDF)

# Cleanup HTML temp
os.remove(html_tmp)

file_size = os.path.getsize(OUTPUT_PDF)
print(f"Done! PDF saved: {OUTPUT_PDF} ({file_size/1024:.0f} KB)")
