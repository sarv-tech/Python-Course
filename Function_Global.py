# Using the global Keyword
# To modify a global variable inside a function, use the global keyword:


def sum(a, b):
    print("I am Sarvesh ")
    c = a + b
    global z   # Please Modify global z
    z = 0   # This will refer to global z and not create a local variable
    return c

z = 3
print(sum(3, 12))
print(z)

print("\n")

x = 10  # Global variable

def modify_global():
    global x
    x = 5  # Modifies the global x

modify_global()
print(x) 


# --------Excessive use of global is discourage as it can make debugging harder.--------------------