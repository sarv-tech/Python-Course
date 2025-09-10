# Functions help in reusability and modularity in Python.


# Syntax :-
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  


# Average of 3 Numbers Using pass, call & print 
def average(a, b, c):
    d = (a + b + c) / 3
    print(d)
average(2, 3, 4)

print("\n")

# Using Return value back
def average(a, b, c):
    d = (a + b + c) / 3
    return d

o1 = average(2, 2, 2)
o2 = average(1, 3, 3)

print(o1)
print(o2)


# Defined using def keyword.
# Function name should be meaningful.
# Use return to send a value back.

