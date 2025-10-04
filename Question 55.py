# Q. Create a base class Animal with a method sound() that prints "Some sound". Create a derived class Dog that overrides sound() to print "Bark!" & Create an object of Dog and call sound().


class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark!")

d = Animal()
d.sound()

d = Dog()
d.sound()  

# The Dog class overrides the sound method of the Animal class to provide its own implementation.
# When we create an object of the Dog class and call the sound method, it prints "Bark!" instead of "Some sound".


