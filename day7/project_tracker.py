# project_tracker.py
# Demonstrates a class, object creation, and a method


class Project:
    def __init__(self, name: str, technology: str, status: str):
        self.name = name
        self.technology = technology
        self.status = status

    def get_details(self) -> str:
        """Returns formatted project information"""
        return (
            f"Project Name: {self.name}\n"
            f"Technology: {self.technology}\n"
            f"Status: {self.status}"
        )


# Create object
project1 = Project(
    "Student Management System",
    "Python",
    "In Progress"
)

# Print project details
print("Project Information")
print("-" * 30)
print(project1.get_details())