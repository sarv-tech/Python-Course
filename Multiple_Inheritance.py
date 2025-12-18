# Multiple Inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary        # Instance attribute for Teacher

class Student:
    def __init__(self, CGPI):
        self.CGPI = CGPI            # Instance attribute for Student

class TA(Teacher, Student):
    def __init__(self, salary, CGPI, name):
        super().__init__(salary)      # Call Teacher's constructor using super()
        Student.__init__(self, CGPI)        # Explicitly call Student's constructor
        Student.name = name                 # Instance attribute specific to TA

ta1 = TA(15000, 8.00, "Sarvesh")        # Creating Object TA
print(ta1.name, ta1.salary, ta1.CGPI)