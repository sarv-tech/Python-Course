# Q. Design a program to continuously take input from the user and print whether the number is positive or negative.The program should stop when the user enters "Quit".

while True:
    user = input("Enter a number or type Quit to stop: ")

    if user == "Quit":
        print("Program stopped")
        break

    number = int(user)

    if number > 0:
        print("Number is Positive")
    elif number < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")
