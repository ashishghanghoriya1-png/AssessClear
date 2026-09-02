# -*- coding: utf-8 -*-
import os
import json

os.makedirs("scratch/conversations", exist_ok=True)

conversations = {
    "conv_master_synthesis.json": {
        "title": "Master Executive & Technical Pre-Pilot Synthesis",
        "timestamp": "2026-08-31 14:00:00",
        "description": "Pre-pilot evaluation across Katni, Indore, Bhopal, and Raisen (351 students).",
        "messages": [
            {
                "role": "user",
                "content": "What is the primary readiness verdict for AssessClear pre-pilot across Madhya Pradesh?"
            },
            {
                "role": "assistant",
                "content": "### 📊 Pre-Pilot Readiness Verdict: Conditional Green Light (Requires Attention Before Pilot)\n\n**Executive Summary:**\nAssessClear demonstrated strong diagnostic value across 9 schools (~351 students in Katni, Indore, Bhopal, and Raisen). However, critical vision auto-crop defects and teacher review latency must be resolved before state-wide pilot deployment.\n\n**Key Strengths:**\n- **Multi-tiered feedback:** Clear pedagogical breakdown ('What you did well', 'Think about this', 'Next steps').\n- **Partial attempt scoring:** Diagnostic weighting (1.0, 0.75, 0.40, 0.0) rewards partial math reasoning.\n- **Hindi OCR Alignment:** Strong support for handwritten Hindi answer sheets.\n\n**Critical Blockers to Resolve:**\n1. **Vision Auto-Crop:** Bounding boxes clip top/bottom headers, skipping Q1 and Q2.\n2. **Review Overhead:** Teachers spend 1.5–3.5 mins per paper reviewing AI outputs.\n3. **Zero-Network Stall:** Complete stoppage in rural schools like MS Kharbai (Raisen).\n4. **Database 200-Cap:** 200-evaluation limit purged 59.3% of history in Katni."
            },
            {
                "role": "user",
                "content": "What are the compute economics and target latency per evaluation?"
            },
            {
                "role": "assistant",
                "content": "### 💰 Compute Economics & Latency Benchmarks\n\n- **Target Cost per Evaluation:** **₹0.12** using Gemini-3.1-Flash-Lite (or local Qwen GPU execution).\n- **AI Processing Latency:** Mean **38.9 seconds** per answer sheet (Indore: 22.8s, Katni: 26.6s, Bhopal: 73.4s).\n- **Teacher Review Latency:** Mean **144.5 seconds** per answer sheet.\n- **Total End-to-End Latency:** **183.4 seconds** per student sheet.\n\n*Optimizing the workflow with a Class Summary Heatmap UI is projected to slash total review time from 122 mins to under 24 mins per 40-student class (81% time reduction).*"
            }
        ]
    },
    "conv_katni_indore_findings.json": {
        "title": "District Empirical Observations: Katni & Indore",
        "timestamp": "2026-08-31 14:15:00",
        "description": "Granular field observations, OCR error rates, and teacher feedback from Katni and Indore.",
        "messages": [
            {
                "role": "user",
                "content": "What specific issues were observed during the Indore and Katni pre-pilots?"
            },
            {
                "role": "assistant",
                "content": "### 🗺️ Granular Findings: Indore & Katni Pre-Pilots\n\n#### **1. Indore (Subhash Nagar MS 108 & Nandbag - 100 Students)**\n- **Observer:** Smt. Deepti Khandelwal (DIET Indore).\n- **Rapid Upload:** Uploading up to 10 sheets worked smoothly (20-30s per sheet).\n- **AI Rigidness Failure:** Question asked for '90 days'; student wrote '3 months'. AI strictly marked it wrong.\n- **Vision Crop Drop:** Q1 and Q2 on page 1 were consistently auto-cropped out (only 7 out of 10 questions evaluated).\n- **Teacher Feedback:** AI must be positioned as a **Teacher Support Tool**, not a teacher replacement.\n\n#### **2. Katni (EPES Purwar & MS Devri Hatai - 91 Students)**\n- **Data Loss Rate:** 59.3% of historical data was purged due to the 200-evaluation database cap.\n- **Digit OCR Misreads:** 5.1% error rate on handwritten numbers (e.g., misreading '9996' as '3226').\n- **Review Latency:** 208 seconds average review time per paper due to slow manual corrections."
            }
        ]
    },
    "conv_tabfm_ml_analysis.json": {
        "title": "Google TabFM Machine Learning Risk & Latency Models",
        "timestamp": "2026-08-31 14:30:00",
        "description": "Zero-shot classification, regression time scaling, and rural network zero-shot simulation.",
        "messages": [
            {
                "role": "user",
                "content": "How does the Google TabFM Classifier predict student risk tiers?"
            },
            {
                "role": "assistant",
                "content": "### 🤖 Google TabFM Zero-Shot Classifier\n\nGoogle's Tabular Foundation Model (TabFM) performs zero-shot risk triage over student evaluation tabular features without model fine-tuning:\n\n1. **High Remedial Risk (Orange/Red):** Triggered when student rubric weight score is < 0.50 or attendance < 65%. Automatically dispatches Sakhi AI WhatsApp remedial modules.\n2. **Critical Blocker (Red):** Triggered when network quality is `No_Network_Zero` (e.g., MS Kharbai, Raisen), locking out mobile PWA ingestion.\n3. **Low Risk / On-Track (Green):** Triggered when rubric score >= 0.70 with steady attendance (>75%)."
            }
        ]
    },
    "conv_action_roadmap_p0_p3.json": {
        "title": "Master Engineering Roadmap (P0 - P3 Priorities)",
        "timestamp": "2026-08-31 14:45:00",
        "description": "Categorized engineering action plan to prepare AssessClear for district rollout.",
        "messages": [
            {
                "role": "user",
                "content": "What are the P0 critical action items required before pilot rollout?"
            },
            {
                "role": "assistant",
                "content": "### 🛠️ P0 Critical Pre-Pilot Action Items\n\n| Item | Target Root Cause | Expected Impact | Timeline |\n|---|---|---|---|\n| **1. Fix Vision Auto-Crop** | Bounding boxes clip top/bottom headers | Lifts question detection from 89.6% to >99.0% | Week 1 |\n| **2. Offline-First PWA Caching** | Zero-network stall in MS Kharbai (Raisen) | Eliminates 10% critical blocker failure | Week 1 |\n| **3. Refactor DB Schema** | Tracks question IDs instead of student copies | Eliminates 59.3% data loss rate in Katni | Week 1 |\n| **4. Blur Quality Gate** | AI hallucinates scores on blurry images | Prevents corrupt diagnostic data | Week 1 |"
            }
        ]
    }
}

for filename, data in conversations.items():
    filepath = os.path.join("scratch/conversations", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Created seed conversation: {filepath}")

print("All seed conversations generated successfully!")
