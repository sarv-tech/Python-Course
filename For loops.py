# What are For Loops?
# For loops are used to iterate over a sequence (e.g., list, string, range).
# They execute a block of code repeatedly for each item in the sequence.


# Syntax:

# for item in sequence:
    # Code to execute for each item

# Example:

fruits = ["apple", "banana", "cherry"]
 
for fruits in fruits:
    print(fruits)

print("\n")

# Using range():
# The range() function generates a sequence of numbers.
# Example:

for k in range(5):
    print(k)  

print("\n")

for j in range(1,6): # range function goes from 1 to (6-1) i.e. 5 in this case.
    print(j)

print("\n")

# Table of 5
for i in range(1,11): 
    print("5 X", i,"=",5*i)