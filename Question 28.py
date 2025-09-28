# Take a user input string and check if it is a palindrome (same forwards and backwards).

str1 = "madam"

if str1 == str1[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
