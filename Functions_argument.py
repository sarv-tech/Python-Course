# Positional Arguments
def add(a, b):
    return a + b

x = add(1, 3)
print(x)


print("\n")
 
# Default Arguments
def add(a, b, plus = 0):
    c = a + b + plus
    return c

x = add(1, 2, 3)   # a=1, b=2, plus=3
print(x)


print("\n")

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  

print("\n")

# Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")