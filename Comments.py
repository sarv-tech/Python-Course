# Comments :-

# Comments are used to explain code and are ignored by the Python interpreter.
# Single-line comments start with #.
# Multi-line comments are enclosed in ''' or """.

# This is a single-line comment
'''
This is a
multi-line comment
'''

# This is a single-line comment
print("Hello, Python!") # This is an inline comment on the same line as code

# This is the first line of a multi-line comment.
# This is the second line.
# This comment explains a block of code.
x = 10
y = 20
print(x + y)

"""
This is a multi-line comment using triple double quotes.
It can span across multiple lines and is often used for documentation (docstrings).
"""

'''
This is another example of a multi-line comment
using triple single quotes.
'''

def greet(name):
    """
    This function takes a name as input and prints a greeting.
    This is a docstring explaining the function's purpose.
    """
    print(f"Hello, {name}!")

greet("Alice")