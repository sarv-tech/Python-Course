# Q. Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("It is an Even number.")
elif num % 2 != 0:   
    print("It is an Odd number.")
else:
    print("Invalid input.")

# num % 2 == 0 indicates number is divisible by 2 so, it is an Even number.
# num % 2 != 0 indicates number is not divisible by 2 so, it is an Odd number.