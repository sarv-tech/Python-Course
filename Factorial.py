# WAP to find the factorial of a number using a function.

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

num = int(input("Enter a number to find its factorial: "))
print("The factorial of", num, "is", factorial(num))
