# Q. Write a program that keeps asking the user to enter a password until they enter the correct one.

# 1st approach
correct_password = "Sarvesh@123"
user_password = input("Enter the password: ")

if correct_password == user_password:
    print("Access granted")
elif correct_password != user_password:
        print("Access denied, try again")
else:
    print("Sign up later")



# 2nd approach
password = "Sarvesh@123"
Entered_password = input("Enter the password: ")

while (Entered_password != password):
    Entered_password = input("Incorrect password. Please try again: ")
print("Access granted, You are login!")