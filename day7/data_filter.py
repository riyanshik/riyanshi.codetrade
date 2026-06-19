# data_filter.py
# Demonstrates column selection and filtering in Pandas

import pandas as pd
import os

# Get current script folder
current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "students.csv")

# Load dataset
df = pd.read_csv(csv_path)

print("Full Dataset:")
print(df)

# Select specific columns
print("\nSelected Columns (name, math_score):")
print(df[["name", "math_score"]])

# Filter 1: Students with math score > 80
print("\nStudents with math score > 80:")
print(df[df["math_score"] > 80])

# Filter 2: Students from Delhi
print("\nStudents from Delhi:")
print(df[df["city"] == "Delhi"])

print("\nFilter Notes:")
print("Filter 1 -> Shows students scoring above 80 in Math")
print("Filter 2 -> Shows only students from Delhi")