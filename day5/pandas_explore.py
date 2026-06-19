# pandas_explore.py
# This program demonstrates Pandas DataFrames,
# filtering, aggregation, and sorting.

import pandas as pd

# Create student dataset
students = {
    "name": [
        "Aditi", "Riya", "Aman", "Rahul", "Priya",
        "Karan", "Neha", "Arjun", "Simran", "Rohit"
    ],
    "city": [
        "Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai",
        "Jaipur", "Delhi", "Pune", "Pune", "Mumbai"
    ],
    "math_score": [82, 67, 91, 74, 88, 79, 60, 95, 72, 85],
    "science_score": [78, 73, 89, 70, 92, 80, 65, 94, 75, 81],
    "english_score": [85, 69, 84, 76, 90, 82, 70, 91, 78, 88]
}

# Create DataFrame
df = pd.DataFrame(students)

print("Student Data:")
print(df)

# Create total score column
df["total_score"] = (
    df["math_score"]
    + df["science_score"]
    + df["english_score"]
)

# 1. Average score in each subject
print("\n1. Average score in each subject:")
print(df[["math_score", "science_score", "english_score"]].mean())

# 2. Student with highest total score
print("\n2. Student with highest total score:")
print(df.loc[df["total_score"].idxmax()])

# 3. Number of students from each city
print("\n3. Students from each city:")
print(df.groupby("city").size())

# 4. Students with math score above 75
print("\n4. Students with math score above 75:")
print(df[df["math_score"] > 75])

# Explore:
# df.nlargest() returns rows with largest values in a column

print("\nTop 3 students by total score:")
print(df.nlargest(3, "total_score")[["name", "total_score"]])