# Q. Create a base class Vehicle with attributes like Brand and Model. Create two subclasses Car and Bike that add extra attributes - seat (in Car) & engine_cc (in Bike).



class Vehicle:                       # base class/ super class/ parent class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):                    # child class
    def __init__(self, brand, model, seat):
        super().__init__(brand, model)    # call parent constructor
        self.seat = seat

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

c = Car("TATA", "Nexon", 4)
b = Bike("Yamaha", "R15", 155)

print(f"  Car Brand: {c.brand},   Car Model: {c.model},      Car Seat: {c.seat}")
print(f" Bike Brand: {b.brand},  Bike Model: {b.model},   Bike Engine: {b.engine_cc}")
