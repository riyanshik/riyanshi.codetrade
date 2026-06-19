# student_profile.py
# Demonstrates dictionaries, f-strings, and type hints


def create_profile(profile: dict) -> str:
    """Returns a formatted profile card."""

    return (
        f"Name: {profile['name']}\n"
        f"Age: {profile['age']}\n"
        f"Course: {profile['course']}\n"
        f"Skills: {', '.join(profile['skills'])}"
    )


# Student profile data
student = {
    "name": "Riyanshi",
    "age": 20,
    "course": "ai ml",
    "skills": ["Python", "Git", "Problem Solving"]
}

print("Student Profile Card")
print("-" * 47)
print(create_profile(student))