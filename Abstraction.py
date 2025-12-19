from abc import ABC, abstractmethod

class Animal(ABC):      # Abstract Base Class

    @abstractmethod
    def make_sound(self):    # Abstract method
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")
        
# Creating objects of child classes
lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()