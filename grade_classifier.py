# Student grade classifier

students = [
    {"name": "Aditi", "score": 90},
    {"name": "Rahul", "score": 70},
    {"name": "Neha", "score": 50},
    {"name": "Aryan", "score": 30},
    {"name": "Riya", "score": 85}
]

def classify(score):

    if score >= 90:
        return "A"

    elif score >= 75:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 40:
        return "D"

    else:
        return "F"

# sorted() with key=lambda sorts using student score
sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

for student in sorted_students:

    grade = classify(student["score"])

    print(student["name"], "-", student["score"], "-", grade)