# student_report.py
# This program demonstrates Object-Oriented Programming (OOP) in Python.
# It defines a Student class with attributes for name, roll number, and marks.
# The class provides methods to calculate the average marks, determine the grade,
# and display a formatted report card for each student.

class Student:
    # Class variable shared by all Student objects
    school_name = "CodeTrade Academy"

    def __init__(self, name, roll_no, marks):
        # Instance variables unique to each student
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
        # Calculate and return the average marks
        return sum(self.marks) / len(self.marks)

    def grade(self):
        # Determine the grade based on the average marks
        avg = self.average()
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

    def __str__(self):
        # Return a formatted report card string
        return (
            f"School: {Student.school_name}\n"
            f"Name: {self.name}\n"
            f"Roll No: {self.roll_no}\n"
            f"Marks: {self.marks}\n"
            f"Average: {self.average():.2f}\n"
            f"Grade: {self.grade()}\n"
        )


# Create three Student objects
student1 = Student("Riya", 101, [92, 88, 95])
student2 = Student("Aman", 102, [78, 82, 80])
student3 = Student("Priya", 103, [65, 70, 68])

# Print the report card for each student
print(student1)
print(student2)
print(student3)