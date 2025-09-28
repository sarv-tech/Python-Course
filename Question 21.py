# Q. Given text = "Python Programming", do the following:
# Print the first 6 characters
# Print the last 6 characters
# Print every second character from the string


text = "Python Programming"

print("The First 6 characters :", text[0:6]) 
print("The Last 6 characters :", text[-6:])
print("Every second character from the string:",text[::2])   # [start : end : step]


# text[::2] means to take every second character from the string, starting from the beginning to the end. The step value of 2 indicates that we want to skip one character and take the next one. So, it effectively selects characters at even indices (0, 2, 4, etc.) from the string. 