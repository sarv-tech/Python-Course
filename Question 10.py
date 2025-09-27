# Q. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")   
elif num == 0:
    print("The number is zero.")
else:
    print("Invalid input.")


# num > 0 indicates that number is bigger than zero and its positive.
# num < 0 indicates that number is smaller than zero and its negative.
# num == 0 indicates that number is equal to zero.

