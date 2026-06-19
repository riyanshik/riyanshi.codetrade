# file_records.py
# This program demonstrates File I/O using the csv module.
# It creates a students.csv file, reads student records,
# calculates average marks and grades, and writes the results
# to a new CSV file named results.csv.

import csv

# Sample student data
students_data = [
    ["Riya", 92, 88, 95],
    ["Aman", 78, 82, 80],
    ["Priya", 65, 70, 68]
]

# Step 1: Create students.csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "math", "science", "english"])
    writer.writerows(students_data)

# Function to determine grade
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Step 2 and 3: Read students.csv and write results.csv
with open("students.csv", "r") as infile, open("results.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)

    fieldnames = ["name", "average", "grade"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        avg = (
            int(row["math"]) +
            int(row["science"]) +
            int(row["english"])
        ) / 3

        writer.writerow({
            "name": row["name"],
            "average": round(avg, 2),
            "grade": get_grade(avg)
        })

print("students.csv created successfully.")
print("results.csv generated successfully.")