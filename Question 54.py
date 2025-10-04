# Q. Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes. Create an object and print the person’s name and age.


class Person:            # defining a class named Person

    def __init__(self, name, age):        # constructor with parameters name and age
        self.name = name       # instance attribute
        self.age = age         # instance attribute

p1 = Person("Sarvesh", 19)       # creating an object of Person class
print(p1.name)
print(p1.age)         # printing the name and age attributes of the object
