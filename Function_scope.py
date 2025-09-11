# In Python, variables have scope (where they can be accessed) and lifetime (how long they exist). Variables are created when a function is called and destroyed when it returns. Understanding scope helps avoid unintended errors and improves code organization.

# Types of Scope in Python
# Local Scope (inside a function) – Variables declared inside a function are accessible only within that function.
# Global Scope (accessible everywhere) – Variables declared outside any function can be used throughout the program.



def sum(a, b):
    # a and b are local variables
    c = a + b
    z = 1   # It creates a local variable called z which is destroyed after this function returns.
    return c

def greet():
    z = 32    # Local Variable
    print("Hello")

z = 8    # z is a global Variable
print(z)
print(sum(4, 6))
print(z)


print("\n")


x = 10    # Global variable

def my_func():
    x = 5      # Local variable
    print(x)  

my_func()
print(x)   # (global x remains unchanged)