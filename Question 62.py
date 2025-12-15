# Q. Write a program to check whether two lists share no common elements


list1 = list(map(int, input("Enter elements of first list: ").split()))

list2 = list(map(int, input("Enter elements of second list: ").split()))

if set(list1).intersection(set(list2)):       # list can be converted into set because it is mutable
    print("Common Elements")
else:
    print(" No Common Elements")
