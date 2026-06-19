# insights.py
# Demonstrates describe() and value_counts()

import pandas as pd
import os

# Get current script folder
current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "students.csv")

# Load dataset
df = pd.read_csv(csv_path)

print("Dataset:")
print(df)

# Numeric summary
print("\nNumeric Summary using describe():")
print(df[["math_score", "science_score"]].describe())

# Categorical summary
print("\nCity Counts using value_counts():")
print(df["city"].value_counts())

# Simple observations
print("\nObservations:")

math_avg = df["math_score"].mean()
print(f"Average Math Score ≈ {math_avg:.2f}")

most_common_city = df["city"].value_counts().idxmax()
print(f"Most common city: {most_common_city}")

print(
    "describe() shows statistics like mean, min, max, and quartiles."
)

print(
    "value_counts() shows how often each category appears."
)
