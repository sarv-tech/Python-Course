# Q. Design & Create an Online Store for Products (name,price).
# Track total products being created.
# Create a static method to calculate discount on each product based on % parameter.



class Product:
    count = 0

    def __init__(self, name, price):  # Constructor
        self.name = name              # instance attribute
        self.price = price
        Product.count += 1

    def get_info(self):             # instance method
        print(f"The price of {self.name} is Rs {self.price}")

    @classmethod               # class Decorator
    def get_count(cls):        # class method
        print(f"Total Products in store = {cls.count}")

    @staticmethod                             # Static Decorator
    def calc_discount(price, discount):       # static Method
        print(f"Discounted price = {price - (price * discount / 100)}")

p1 = Product("i phone 15", 60000)     # object (instance) created from the class
p2 = Product("Mac Book", 200000)
p3 = Product("watch", 1100)

p1.get_info()                         # call of instance method using object
Product.get_count()                   # call of class method using class
Product.calc_discount(42000, 10)      # Call from static method