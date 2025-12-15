# Q. Given list of tuples with info(name, subject):
# 1. list all unique course
# 2. list students enrolled in English
# 3. create dictionary (student, set of courses)


info = [
    ("Alice", "Math"),
    ("Bob", "English"),
    ("Alice", "English"),
    ("Charlie", "Science"),
    ("Bob", "Math")
]

unique_courses = set()

for name, subject in info:
    unique_courses.add(subject)

print(unique_courses)

english_students = []

for name, subject in info:
    if subject == "English":
        english_students.append(name)

print(english_students)

student_courses = {}

for name, subject in info:
    if name not in student_courses:
        student_courses[name] = set()
    student_courses[name].add(subject)

print(student_courses)
