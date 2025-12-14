# WAP to count and print all the vowels in a given word.

count = 0
word = 'artificial'

for ch in word:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print(ch)
        count += 1
        print("Count:", count)