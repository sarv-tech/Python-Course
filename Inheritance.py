# Inheritance is like a family tree. A child class (or subclass) inherits traits (attributes and methods) from its parent class (or superclass). This allows you to create new classes that are specialized versions of existing classes, without rewriting all the code.

# super(): Inside a child class, super() lets you call methods from the parent class. This is useful when you want to extend the parent's behavior instead of completely replacing it. It's especially important when initializing the parent class's part of a child object.

class Animal :      # Parent class or Super class
    location = "Earth"         # Class attribute

    def __init__(self, name) :       # Constructor
        self.name = name       # Instance attribute
    def speak(self) :                       # Method of parent class
        print("Animal speaks.....")         

class Dog(Animal) :      # Child class or Sub class
    def speak(self) :              # Method of child class
        super().speak()          # Calling parent class method
        print("Dog barks.....")

a = Animal("Leo")       # Creating object of parent class
a.speak()            # Calling method of parent class

d = Dog("Tommy")         # Creating object of child class
d.speak()            # Calling method of child class




# Polymorphism, as we saw with the speak() method in the inheritance example, means that objects of different classes can respond to the same method call in their own specific way. This allows you to write code that can work with objects of different types without needing to know their exact class.