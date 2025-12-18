class Employee:
    Start_Time = "10 am"     # class variable
    End_Time = "6 pm"        # class variable

    def change_time(self, new_end_time):
        self.End_Time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):      
        self.subject = subject          # Instance Variable

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role               # Instance Variable

t1 = Teacher("English")              # Creating Teacher object
t1.change_time("12 pm")
print(t1.subject, t1.Start_Time, t1.End_Time)

staff1 = AdminStaff("Manager")             # creating AdminStaff object
print(staff1.role, staff1.Start_Time, staff1.End_Time)