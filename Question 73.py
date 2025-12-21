# Q. Create a class Shape with a method area(). Create subclasses Circle, Rectangle, and Triangle that override the area() method.

class Shape:                              
    def get_area(self):                 # Parent Class Method. 
        print("area = Shape")           # This method will overridden by child classes

class Circle(Shape):
    def get_area(self):                 # Child class Circle overrides get_area() method
        print("area = Circle")

class Rectangle(Shape):
    def get_area(self):                  # Child class Rectangle overrides get_area() method
        print("area = Rectangle")

class Triangle(Shape):
    def get_area(self):                  # Child class Triangle overrides get_area() method
        print("area = Triangle")

c = Circle()                             # Creating object of Circle class
c.get_area()                             # Calls Circle get_area() method

r = Rectangle()                          # Creating object of Rectangle class
r.get_area()                             # Calls Rectangle get_area() method

t = Triangle()                           # Creating object of Triangle class
t.get_area()                             # Calls Triangle get_area() method