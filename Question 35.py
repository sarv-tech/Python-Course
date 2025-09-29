# Q. Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?) & Add 5 to the set, remove 2, and check if 4 is in the set.


my_set = {1, 2, 3, 3, 4}
print(my_set)  # Output will be {1, 2, 3, 4} since sets do not allow duplicate values. Duplicate 3 is automatically removed in a set. 

my_set.add(5)  # Adding an element to the set
print(my_set)  
my_set.remove(2)  # Removing an element from the set
print(my_set)

# Checking if 4 is in the set
check = 4 in my_set
print(check)   # yes its True 