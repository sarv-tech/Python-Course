# Q. Create the following classes : Herbivore, Carnivore, Omnivore with some attributes & methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.


class Herbivore:
    def __init__(self, plants):
        self.plants = plants            # Instance attribute for Herbivore

class Carnivore:
    def __init__(self, meat):
        self.meat = meat                   # Instance attribute for Carnivore

class Omnivore:
    def __init__(self, plants, meat):
        self.plants = plants
        self.meat = meat                  # Instance attribute for Omnivore

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, plants, meat, name):
        super().__init__(plants)              # calls Herbivore Constructor using super()
        Carnivore.__init__(self, meat)              # calls Carnivore constructor
        Omnivore.__init__(self, plants, meat)
        self.name = name                           # Bear's own attribute

b = Bear("Berries", "Seal", "Polar Bear")          # creating Object Bear
print(f"{b.name} eat plants = {b.plants} & in meat = {b.meat}")
