# WAP to take username and password as input from the user and check if the credentials are correct. 

username = input("Enter your username: ")
password = input("Enter your password: ")

if (username =="admin" and password == "pass"):
    print("Login successful!")
elif(username != "admin"):
    print("wrong Username")
else:
    print("wrong Password")