class Student:
    College = "Ramrao Adik Institute Of Technology"         # Class Attribute
    PI = 3.14

    def __init__(self, name, CGPI):
        self.name = name          # Instance Attribute
        self.CGPI = CGPI
        self.PI = 3.14

stud1 = Student("Sarvesh", 8.00)
print(stud1.name)
print(stud1.PI)
print(Student.College)