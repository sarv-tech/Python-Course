# Q. Create an abstract class Employee with an abstract method calculate_salary(). Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.


from abc import ABC, abstractmethod            # for abstract class

class Employee(ABC):                           # abstract parent class

    @abstractmethod
    def calculate_salary(self):                # abstract method
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("Salary = Stipend Based")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary = Monthly fixed salary")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Salary = Hourly Based")


I = Intern()                                    # object of Intern
I.calculate_salary()                            # calls Intern method

F = FullTimeEmployee()                          # object of FullTimeEmployee
F.calculate_salary()                            # calls FullTimeEmployee method

c = ContractEmployee()                          # object of ContractEmployee
c.calculate_salary()                            # calls ContractEmployee method