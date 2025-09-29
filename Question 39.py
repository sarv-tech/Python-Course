# Q. Write a program that takes a list of numbers and removes all duplicates using a set.

my_list = [2, 1, 2, 4, 3, 4, 5]

# Using set to remove duplicates
my_set = set(my_list)
# Converting back to list
unique_list = list(my_set)
print(unique_list)
