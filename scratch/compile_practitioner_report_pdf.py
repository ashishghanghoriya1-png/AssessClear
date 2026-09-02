# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

# Read practitioner report markdown
md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "C:\\Users\\Peepul\\.gemini\\antigravity\\brain\\695dad16-060c-40a2-a197-2f8f545292f1\\practitioner_summary_report.md")

if not os.path.exists("scratch/practitioner_summary_report.md"):
    with open(md_path, "r", encoding="utf-8") as rf:
        report_text = rf.read()
    with open("scratch/practitioner_summary_report.md", "w", encoding="utf-8") as wf:
        wf.write(report_text)
else:
    with open("scratch/practitioner_summary_report.md", "r", encoding="utf-8") as rf:
        report_text = rf.read()

# Build elegant HTML for PDF conversion
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Field Synthesis & Strategic Review: Sakhi AI & AssessClear</title>
<style>
  @page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
  }}
  body {{
    font-family: 'Georgia', 'Times New Roman', serif;
    color: #1a1a1a;
    line-height: 1.65;
    font-size: 11.5pt;
    margin: 0;
    padding: 0;
  }}
  .header {{
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 12px;
    margin-bottom: 24px;
  }}
  h1 {{
    color: #1e3a8a;
    font-size: 22pt;
    margin: 0 0 8px 0;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 700;
  }}
  .meta {{
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 10pt;
    color: #4b5563;
    margin-bottom: 4px;
  }}
  h2 {{
    color: #1e3a8a;
    font-size: 14pt;
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 4px;
    margin-top: 22px;
    margin-bottom: 12px;
    font-family: 'Helvetica Neue', Arial, sans-serif;
  }}
  p {{
    margin-top: 0;
    margin-bottom: 14px;
    text-align: justify;
  }}
  strong {{
    color: #111827;
  }}
  .footer {{
    margin-top: 30px;
    border-top: 1px solid #e5e7eb;
    padding-top: 10px;
    font-size: 9pt;
    color: #6b7280;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    text-align: center;
  }}
</style>
</head>
<body>

<div class="header">
  <h1>Field Synthesis & Strategic Review</h1>
  <div class="meta"><strong>Topic:</strong> Sakhi AI & AssessClear Digital Interventions in Government Middle Schools</div>
  <div class="meta"><strong>Prepared by:</strong> Senior Education & Policy Advocacy Specialist</div>
  <div class="meta"><strong>Context:</strong> Pre-Pilot Diagnostic Evaluation across Katni, Indore, Bhopal, & Raisen, Madhya Pradesh</div>
</div>

{report_text.replace('# Field Synthesis & Strategic Review: Sakhi AI & AssessClear Digital Interventions', '').replace('**Prepared by:** Senior Education & Policy Advocacy Specialist  \n**Target Audience:** Project Leadership, Government & CSR Steering Committee  \n**Context:** Pre-Pilot Diagnostic Evaluation in Government Middle Schools (Grades 6–8), Madhya Pradesh  \n\n---', '').replace('## ', '<h2>').replace('\n\n', '</p><p>').replace('<h2>', '</p><h2>')}

<div class="footer">
  AssessClear & Sakhi AI Pre-Pilot Evaluation Report · Prepared for State Education Leadership & Steering Committee (September 2026)
</div>

</body>
</html>
"""

html_path = os.path.abspath("scratch/practitioner_report.html")
pdf_path = os.path.abspath("Practitioner_Field_Synthesis_and_Strategic_Review.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

browser = edge if os.path.exists(edge) else chrome
url = 'file:///' + html_path.replace('\\', '/')

cmd = [
    browser,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}',
    url
]

res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_path):
    print(f"SUCCESS: PDF created at {pdf_path} (Size: {os.path.getsize(pdf_path)} bytes)")
else:
    print("ERROR: PDF creation failed")
