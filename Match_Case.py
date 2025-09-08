# What is Match-Case?
# Match-case is a new feature introduced in Python 3.10 for pattern matching.
# It simplifies complex conditional logic.

# Syntax
# match value:
#     case pattern1:
#          Code to execute if value matches pattern1
#     case pattern2:
#          Code to execute if value matches pattern2
#     case _:
#          Default case (if no patterns match)



a = int(input("Enter the number between 1 and 10: "))

match a:
    case 1: 
        print("You won a ps5")
    case 3:
        print("You won a $228")
    case 5:
        print("You won a Cricket Kit")
    case 7: 
        print("You won a Hp Charger")
    case _:
        print("Better Luck Next Time :( ")



status = 404

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")