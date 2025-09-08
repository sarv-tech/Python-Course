age = int(input("Enter Your age: "))

if(age>18):
    print("You can drive")
elif(age == 18):
    print("Let's Schedule an Interview")
elif(age == 0):
    print("Hey! kiddo, Just now you are born")
else:
    print("Sorry,You Cannot Drive")