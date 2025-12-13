# WAP to count the number of times 'i' appears in the word "artificial intelligence".

word = "artificial intelligence"

count = 0

for ch in word:
    if ch == 'i':
        count += 1
print("The count of 'i' in the word is:", count)