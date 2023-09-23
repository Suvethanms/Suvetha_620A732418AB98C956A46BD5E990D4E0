#challenge 3.2

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa,reverse=True)
    return sorted_students

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
students_list = [
    Student("suve", "2023001", 3.9),
    Student("Janani", "2023002", 3.7),
    Student("karunya", "2023003", 3.8),
    Student("priya", "2023004", 3.6)
]

sorted_students = sort_students(students_list)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
