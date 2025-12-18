# Multi-level inheritance

class Employee:
    # Class variables (shared by all employees)
    start_Time = "10 am"
    End_Time   = "6 pm"


class AdminStaff(Employee):
    def __init__(self, role):
        # Instance attribute specific to AdminStaff
        self.role = role


class Accountant(AdminStaff):
    def __init__(self, salary, role):
        # Calls AdminStaff constructor to set role
        super().__init__(role)
        
        # Instance attribute specific to Accountant
        self.salary = salary


# Creating Accountant object
acc1 = Accountant(450000, "Software Engineer")

print(f"Rohan is a {acc1.role} at Amazon and has {acc1.salary} salary per annum and hisreporting time to the office is {acc1.start_Time} to {acc1.End_Time}.")
