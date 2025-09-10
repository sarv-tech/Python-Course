# A function calling itself to solve a problem.

# Example: Factorial using Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  

# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals.

print("\n")

"Recursive Function"
def show(n):
    if n == 0:  # Base case
        return
    print(n)
    show(n-1)

show(5)


print("\n")

# Sum of First n natural numbers
def calc_sum(n):
    if n == 0:   # Base case
        return 0
    return calc_sum(n-1) + n

# call the function
print(calc_sum(10))
