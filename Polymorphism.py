# Function Overriding

class Employee:
    def get_designation(self):
        print("designation = Employee")      # Method of Employee class

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")       # Method of Teacher class

t1 = Teacher()              # Object created of Teacher class
t1.get_designation()      # call method



# Function Duck Typing => Walks like a duck & quacks like a duck 

class Employee():
    def get_designation(self):
        print("designation = Employee")      # Method of Employee class

class Accountant():
    def get_designation(self):
        print("designation = Accountant")     # Method of Accountant Class

e1 = Employee()                   # Creating object of Employee class
e1.get_designation() 

a1 = Accountant()                   # Creating Object of Accountant Class
a1.get_designation()