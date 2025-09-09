# Each character in a string has a unique index, starting from 0 for the first character and -1 for the last character.

name = "Sarvesh0123456789"

print(name[0:2]) # goes from 0 to 2-1 i.e. 1

print(name[2:-1]) # same as [2:16]

# Print (name[0:12:n]) # Skip n-1 characters
print(name[0:12:1]) # Skip 0 Character
print(name[0:12:3]) # Skip 3-1 i.e. 2 characters

print(name[:5]) # Replace the first empty number with 0 same as name[0:5]
print(name[1:]) # Replace the second empty number with length same as name[1:17]

print("\n")

# Slicing allows you to extract a portion of a string using the syntax string[start:stop:step].

text = "Hello, Python!"
print(text[0:5])   
print(text[:5])    
print(text[7:])  
print(text[::2])   
print(text[-6:-1]) 