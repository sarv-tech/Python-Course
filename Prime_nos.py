# Q. Write a function is_prime(n) that returns True if the given number n is a prime number, otherwise returns False. Use a loop to check whether the number is prime.

def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(" It is a Prime number")
else:
    print("It is Not a prime number")