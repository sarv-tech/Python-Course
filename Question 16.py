# Q. Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

num = int(input("Enter a day number (1-7): "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case default:
        print("Invalid day number. Please enter a number between 1 and 7.")

# Explaination: the code prompts the user to input a number between 1 and 7, which corresponds to the days of the week.Then it uses a match-case statement to check the input number and print the corresponding day. If the input number is outside the range of 1 to 7, it prints an error message indicating that the input is invalid.

# match = a control flow statement that allows you to compare a value against multiple patterns and execute code based on which pattern matches. It is similar to switch-case statements found in other programming languages.

# case = a keyword used within a match statement to define a specific pattern to match against the value being evaluated. Each case represents a possible value or condition that the input can take, and the corresponding block of code is executed if the input matches that case.

# default = a keyword used in a match-case statement to define a block of code that will be executed if none of the specified cases match the input value. It serves as a fallback option to handle unexpected or invalid input.
