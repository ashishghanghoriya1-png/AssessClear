# AssessClear: AI Diagnostic Intelligence & Pilot Command Center

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Google TabFM](https://img.shields.io/badge/Model-Google%20TabFM-blue.svg)](https://research.google/)
[![Ollama Local AI](https://img.shields.io/badge/Local%20LLM-Qwen%203%20(14B)-green.svg)](https://ollama.com/)

**AssessClear** is an AI-enabled diagnostic assessment platform designed for government middle school classrooms (Grades 6–8) across Madhya Pradesh. This repository contains the interactive Streamlit command center, cross-district empirical pre-pilot dataset ($N=351$), machine learning models (Google TabFM Classifier & Regressor), and strategic evaluation reports.

---

## 📊 Core Features

1. **Executive Scorecard & Readiness Verdict:**
   - Real-time pre-pilot KPI tracking across 9 government schools in Katni, Indore, Bhopal, and Raisen.
   - Analysis of 4-tier rubrics (1.0, 0.75, 0.40, 0.0) and ₹0.12/eval compute economics.
2. **Interactive District Explorer:**
   - Multi-dimensional cross-filtering by District, Subject (Math, Hindi), Grade (6–8), and School.
   - Processing vs. review latency metrics and granular student-level evaluation datasets.
3. **Google TabFM Machine Learning Playground:**
   - **TabFM Classifier:** Zero-shot student remedial risk tiering (Red / Amber / Green) and misconception classification.
   - **TabFM Regressor:** Time-overhead forecasting and class-size scaling ($N=10$ to $80$ students).
   - **Zero-Shot Simulator:** Scenario simulation for rural tribal schools vs. urban model schools.
4. **Master Strategic Action Roadmap (P0, P1, P2, P3):**
   - Actionable engineering and product priorities addressing vision segmentation, offline PWA caching, and database retention.
5. **Ask Qwen AI Assistant:**
   - Embedded local AI assistant powered by `qwen3:14B` via Ollama GPU acceleration.
6. **PDF Reports Center:**
   - Direct access to all comprehensive evaluation and technical reports.

---

## 🚀 Quickstart

### 1. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/<your-username>/Assessbot.git
cd Assessbot
pip install -r requirements.txt
```

### 2. Run the Streamlit Dashboard
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📑 Generated Evaluation Reports
* `AssessClear_Diagnostic_Intelligence_Pre_Pilot_Evaluation_and_Strategic_Action_Plan.pdf`
* `AssessClear_Master_Executive_and_Technical_Summary.pdf`
* `AssessClear_TabFM_Empirical_Analysis_Report.pdf`
* `AssessClear_Qwen_Direct_Master_Synthesis.pdf`

---

## 🏛️ License
Internal Project Evaluation Repository. Prepared for State Leadership & Deployment Teams (August 2026).
