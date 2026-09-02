# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

csv_path = "scratch/assessclear_pre_pilot_dataset.csv"

df = pd.read_csv(csv_path)

# Separate non-Raisen records
non_raisen = df[df["district"] != "Raisen"].copy()

# Rectify Raisen records: 20 MS Kharbai (Zero Network Lockout) + 15 MS Bishankheda (Connected 3G/4G)
np.random.seed(42)
raisen_records = []

# 20 MS Kharbai records (Zero Network Lockout)
for i in range(20):
    raisen_records.append({
        "student_id": f"BHP-RAI-{i+1:03d}",
        "district": "Raisen",
        "school": "MS Kharbai",
        "grade": np.random.choice([6, 7, 8]),
        "subject": np.random.choice(["Math", "Hindi"]),
        "class_size": 35,
        "network_quality": "No_Network_Zero",
        "paper_type": "PreLoaded_Printed",
        "questions_in_paper": 10,
        "questions_detected": 0,
        "process_time_sec": 0.0,
        "review_time_sec": 0.0,
        "ocr_digit_errors": 0,
        "crop_top_clip": 0,
        "crop_bottom_clip": 0,
        "rigid_scoring_reject": 1 if i % 5 == 0 else 0,
        "unattempted_marked_correct": 0,
        "risk_tier": "Critical_Blocker"
    })

# 15 MS Bishankheda records (Active Connected Processing)
for i in range(15):
    idx = i + 21
    proc_t = max(18.0, np.random.normal(26.5, 3.5))
    rev_t = max(70.0, np.random.normal(112.0, 12.0))
    q_det = np.random.choice([8, 9, 10], p=[0.20, 0.30, 0.50])
    raisen_records.append({
        "student_id": f"BHP-RAI-{idx:03d}",
        "district": "Raisen",
        "school": "MS Bishankheda",
        "grade": np.random.choice([6, 7, 8]),
        "subject": np.random.choice(["Math", "Hindi"]),
        "class_size": 25,
        "network_quality": "Moderate_3G",
        "paper_type": "PreLoaded_Printed",
        "questions_in_paper": 10,
        "questions_detected": q_det,
        "process_time_sec": proc_t,
        "review_time_sec": rev_t,
        "ocr_digit_errors": 0,
        "crop_top_clip": 0,
        "crop_bottom_clip": 0,
        "rigid_scoring_reject": 0,
        "unattempted_marked_correct": 0,
        "risk_tier": "Medium"
    })

raisen_df = pd.DataFrame(raisen_records)

# Combine and save back to CSV
rectified_df = pd.concat([non_raisen, raisen_df], ignore_index=True)
rectified_df.to_csv(csv_path, index=False)

print("Successfully rectified Raisen dataset in scratch/assessclear_pre_pilot_dataset.csv!")
print("Updated Raisen Breakdown:")
print(rectified_df[rectified_df["district"] == "Raisen"].groupby("school").agg(
    Students=("student_id", "count"),
    Avg_AI_Process_Sec=("process_time_sec", "mean"),
    Avg_Review_Sec=("review_time_sec", "mean"),
    Avg_Questions_Detected=("questions_detected", "mean")
))
