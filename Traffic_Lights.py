# WAP which user can input the color of traffic light and program will display appropriate message.

color = input("Enter the Traffic Light Color: ")

if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Get Ready")
elif color == "Green":
    print("Go")
else:
    print("Invalid Color")
    