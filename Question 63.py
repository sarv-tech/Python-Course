# Q. WAP program to ask the user for a string, print all unique characters, and count them.


# Ask user for input
s = input("Enter a string: ")

# Get unique characters using a set
unique_chars = set(s)

# Print unique characters
print("Unique characters:",unique_chars)

# Print count of unique characters
print("Count of unique characters:",len(unique_chars))
