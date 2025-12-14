# Q. Write a function that prints the digits of a number n one by one.
# For example, if n = 312, the digits are 3, 1, and 2, and the program should print them.

def print_digits(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10

num = int(input("Enter a number: "))
print_digits(num)