# Q. Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def sum_of_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_of_digits(n // 10)

# sum of digits of of 7532 is same as :
# 2(last digit) + sum of digits of 753
number = 7532
result = sum_of_digits(number)
print(f"The sum of digits of {number} is {result}")
