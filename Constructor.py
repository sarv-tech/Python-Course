# The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.

class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary      # Create an instance attribute 'salary' and assign it the value of the parameter 'salary'
        self.name = name
        self.bond = bond

    def display(self):
        return self.salary

    def info(self):
        print(f"The name of the employee is {self.name}, Salary is {self.salary} and his bond is {self.bond} years.")

emp1 = Employee(100000, "John", 5)  
emp1.info()  

print("\n")

class Dog:

    def __init__(self, age, breed):  # The constructor
        self.age = age      # Setting the age attribute
        self.breed = breed    # Setting the breed attribute

# When we do this:
my_dog = Dog("16", "Poodle")  # The __init__ method is automatically called

# It's like we're saying:
# 1. Create a new Dog object.
# 2. Run the __init__ method on this new object:
#    - Set my_dog.age to "16"
#    - Set my_dog.breed to "Poodle"

class Dog:
    def __init__(self, name="Unknown", breed="Mixed"):
        self.name = name
        self.breed = breed

dog1 = Dog()          # name will be "Unknown", breed will be "Mixed"
dog2 = Dog("Rex")     # name will be "Rex", breed will be "Mixed"
dog3 = Dog("Bella", "Labrador") # name will be "Bella", breed will be "Labrador"