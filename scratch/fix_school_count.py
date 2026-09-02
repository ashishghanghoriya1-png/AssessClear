# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

csv_path = "scratch/assessclear_pre_pilot_dataset.csv"
df = pd.read_csv(csv_path)

# Map Bhopal schools to the exact 3 Bhopal pilot schools: MS Green Park, MS Putlighar, HS Kanya
bhopal_schools = ["MS Green Park", "MS Putlighar", "HS Kanya"]

bhopal_indices = df[df["district"] == "Bhopal"].index

for i, idx in enumerate(bhopal_indices):
    df.loc[idx, "school"] = bhopal_schools[i % 3]

df.to_csv(csv_path, index=False)

print("Updated Bhopal schools in CSV to exact 3 schools: MS Green Park, MS Putlighar, HS Kanya.")
print("Unique schools per district:")
print(df.groupby("district")["school"].unique())
print(f"Total Unique Schools across dataset: {df['school'].nunique()}")
