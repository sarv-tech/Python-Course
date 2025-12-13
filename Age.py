# WAP to take age as input from the user and print whether the user is a child, a teenager or an adult 

Age_num = int(input("Please enter your age: "))

if (Age_num < 13):
    print("You are a child.")
elif (13 <= Age_num < 18):
    print("You are a teenager.")
elif Age_num >= 18:
    print("You are an adult.")
else:
    print("you are a God!!")