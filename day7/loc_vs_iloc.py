# loc_vs_iloc.py
# Demonstrates the difference between .loc and .iloc

import pandas as pd
import os

# Get path of current script folder
current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "students.csv")

# Load dataset
df = pd.read_csv(csv_path)

print("Dataset:")
print(df)

# -----------------------
# .loc example
# Label-based selection
# Select rows 1 to 3 and columns name + city
# -----------------------

print("\nUsing .loc:")
print(df.loc[1:3, ["name", "city"]])

# -----------------------
# .iloc example
# Position-based selection
# Select rows 1 to 3 and first two columns
# -----------------------

print("\nUsing .iloc:")
print(df.iloc[1:4, 0:2])

# Notes
print("\nDifference:")
print(".loc uses row/column labels (names)")
print(".iloc uses row/column positions (numbers)")