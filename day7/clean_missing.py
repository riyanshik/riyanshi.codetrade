# clean_missing.py
# Demonstrates handling missing values in Pandas

import pandas as pd
import os

# Get current script folder
current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "students_missing.csv")

# Load dataset
df = pd.read_csv(csv_path)

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

# Example 1: drop rows with missing values
dropped_df = df.dropna()

print("\nAfter dropna():")
print(dropped_df)

# Example 2: fill missing values
filled_df = df.copy()

filled_df["math_score"] = filled_df["math_score"].fillna(
    filled_df["math_score"].mean()
)

filled_df["science_score"] = filled_df["science_score"].fillna(
    filled_df["science_score"].mean()
)

print("\nAfter fillna():")
print(filled_df)

# Observations
print("\nNotes:")
print("dropna() removes rows with missing data")
print("fillna() replaces missing values")