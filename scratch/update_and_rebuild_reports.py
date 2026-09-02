# -*- coding: utf-8 -*-
import os, glob, re, subprocess

# Browser finder helper
def get_browser_cmd():
    edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    if os.path.exists(edge):
        return edge
    elif os.path.exists(chrome):
        return chrome
    return "chrome"

browser = get_browser_cmd()

def update_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    # Replace chrome path line
    target_chrome = "chrome = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'"
    replacement_chrome = f"chrome = r'{browser}'"
    code = code.replace(target_chrome, replacement_chrome)

    # Replace Raisen text in table
    old_raisen = "(5 Schools incl. MS Kharbai)"
    new_raisen = "(5 Schools: MS Green Park, MS Putlighar, HS Kanya in Bhopal; MS Kharbai & MS Bishankheda in Raisen)"
    code = code.replace(old_raisen, new_raisen)

    old_raisen_defect = "• Zero network in MS Kharbai halted all scanning."
    new_raisen_defect = "• Zero network in MS Kharbai halted scanning (0s latency), while MS Bishankheda & Bhopal schools processed normally (~26s AI processing)."
    code = code.replace(old_raisen_defect, new_raisen_defect)

    old_raisen_defect2 = "• Zero network in MS Kharbai halted app completely."
    new_raisen_defect2 = "• Zero network in MS Kharbai halted app completely (0s latency), while MS Bishankheda processed normally (~26s)."
    code = code.replace(old_raisen_defect2, new_raisen_defect2)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Updated {filepath}")

update_file("scratch/compile_final_report_pdf.py")
update_file("scratch/generate_master_summary_pdf.py")
update_file("scratch/generate_tabfm_report_and_pdf.py")
update_file("scratch/compile_qwen_direct_master_pdf.py")

print("Finished updating python report scripts!")
