name =  "sarvesh"    # Strings are immutable

# s[0] = "B"  ------> I Cannot do that

a = len(name)
print(a)

# print(name.upper(),name)

# Changing Case
print(name.lower())
print(name.capitalize())
print(name.upper())
print(name.title())

print("\n")

# Removing Whitespace
text = "  hello world  "
print(text.strip())  
print(text.lstrip()) 
print(text.rstrip()) 

print("\n")

# Finding and Replacing
text = "Python is fun"
print(text.find("is"))   
print(text.replace("fun", "awesome"))  

print("\n")

# Splitting and Joining
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  

new_text = " - ".join(fruits)
print(new_text)  

print("\n")

# Checking String Properties
text = "Python123"
print(text.isalpha()) 
print(text.isdigit())  
print(text.isalnum()) 
print(text.isspace())  