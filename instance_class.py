# Class Attributes: These are shared by all objects of the class. Like species in our Dog class. All dogs belong to the same species. They are defined outside of any method, directly within the class.

# Instance Attributes: These are specific to each individual object. name and breed are instance attributes. Each dog has its own name and breed. They are usually defined within the __init__ method.

class Employee:
    Company = "Google"  # Class attribute

    def __init__(self, salary, name, bond, Company):
        self.salary = salary      # Create an instance attribute 'salary' and assign it the value of the parameter 'salary'
        self.name = name
        self.bond = bond
        self.Company = "Microsoft"  # Instance attribute with the same name as class attribute

    def display(self):
        return self.salary

    def info(self):
        print(f"The name of the employee is {self.name}, Salary is {self.salary} and his bond is {self.bond} years.")

emp1 = Employee(100000, "John", 5,"Microsoft")  
print(emp1.Company)  # will always print the instance attribute whenever present

print(Employee.Company)  # This will always print the class attribute

# Object introspection
print(dir(emp1))  # Lists all attributes and methods of the object