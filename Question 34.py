# Q. Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.


my_tuple = (10, 20, 30, 40)

# Convert tuple to list
my_list = list(my_tuple)

# Change the first element to 50
my_list[0] = 50

# Convert list back to tuple
my_tuple = tuple(my_list)

# Print the modified tuple
print(my_tuple)
