# String Formatting

# String formatting is a powerful feature in Python that allows you to insert variables and expressions into strings in a structured way. Python provides multiple ways to format strings, including the older .format() method and the modern f-strings.

template = "Hi {}, Congratulations! You won Grand Finale stage in Smart India Hackathon and you'll be awarded Rs {} cheque."

a = "Sarvesh"
a1 = 100000
b = "Kanishka"
b1 = 25000
c = "Zainab"
c2 = 2500

s1 = template.format(a,a1)
print(s1)

print("\n")

print(f"{a}, You won a CGPI as 8.00 Award of Rs.{c2} cheque.")

print("\n")

# adding and Alignment
text = "Python"
print(f"{text:>10}")  
print(f"{text:<10}")  
print(f"{text:^10}")  


print("\n")

x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}.")

print("\n")


# The .format() method allows inserting values into placeholders {}:
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))


print("\n")

# You can also specify positional and keyword arguments:
print("{1} is learning {0}".format("Python", "Alice"))
print("{name} is {age} years old".format(name="Bob", age=25))



# Escape Sequences: Use \n, \t, \', \", and \\ to handle special characters in strings.

# Raw Strings: Use r"string" to prevent escape sequence interpretation.

# String Encoding & Decoding: Use .encode() and .decode() to work with different text encodings.

# String Immutability: Strings in Python are immutable, meaning they cannot be changed after creation.

# Performance Considerations: Using ''.join(list_of_strings) is more efficient than concatenation in loops.