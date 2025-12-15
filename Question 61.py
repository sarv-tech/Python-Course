# Q. Given a list of words:
#  words =["apple","banana","kiwi","cherry","mango"]
#  Create a dictionary that maps each word to its length

words = ["apple","banana","kiwi","cherry","mango"]
words_length = {}

for ch in words:
    words_length[ch] = len(words)
print(words_length)
