# json_report.py

import json
import os

# Get path of current script
current_folder = os.path.dirname(__file__)
json_path = os.path.join(current_folder, "profile.json")

# Read JSON file
with open(json_path, "r") as file:
    data = json.load(file)

# List comprehension
uppercase_skills = [skill.upper() for skill in data["skills"]]

print("Learner Report")
print("-" * 30)

print(f"Name: {data['name']}")
print(f"Role: {data['role']}")
print(f"Skills: {', '.join(uppercase_skills)}")
print(f"Total Skills: {len(data['skills'])}")