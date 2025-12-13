
color = input("Enter the traffic light color: ")

match color:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Get Ready")
    case "Green":
        print("Go")
    case default:
        print("Invalid color")