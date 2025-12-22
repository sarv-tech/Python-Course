# Q. Create a class Person that allows the constructor to work with :
# • name only
# • name + age
# • name + age + address
# As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.


class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name          # name is mandatory
        self.age = age            # optional parameter
        self.address = address    # optional parameter

    def display(self):
        print(f"Name : {self.name}, Age : {self.age}, Address : {self.address}")

p1 = Person("Sarvesh")                    # name only
p2 = Person("Om", 21)                # name + age
p3 = Person("Rohan", 21, "Mumbai")      # name + age + address

p1.display()
p2.display()
p3.display()
