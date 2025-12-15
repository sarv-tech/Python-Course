# Q. Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string that reads the same forward and backward.


string = str(input("Enter a String: "))

if(string == string[::-1]):    # It reverse a string [: : -1] => start from beginning and step by -1.
    print("Its a palindrome")
else:
    print("Not an palindrone")
    


print("\n")

s = input("Enter a string: ")

rev = ""
for ch in s:
    rev += ch   # add character in front

if s == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
