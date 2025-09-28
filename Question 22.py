# Q. Reverse the string text using slicing.

text =  "Sarvesh"

reverse = text[::-1]
print(reverse)

# text[::-1] means to reverse the string. The slicing syntax [start:end:step] is used here with a step value of -1, which indicates that we want to traverse the string from the end to the beginning, effectively reversing it. So, it takes all characters in the string but in reverse order.