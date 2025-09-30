# Q. Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.


def safe_divide(a,b):       # Function to safely divide two numbers with zero-check 
    if b == 0 :                     # base case to check if b is zero 
        return "Cannot divide by zero"
    else:
        return a/b                 # Perform the division if b is not zero

print(safe_divide(10,2))    # Output: 5.0
print(safe_divide(10,0))    # Output: "Cannot divide by zero"