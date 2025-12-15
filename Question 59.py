# Q. Input two lists of integers from the user, merge them into one list, and sort the result.


list1 = list(map(int,input("Enter an elements: ").split()))
list2 = list(map(int,input("Enter an elements: ").split()))

result = list1 + list2
print(result)

result.sort()
print(result)