# Write a program that counts how many vowels are in a given string.

sentence = "Coding in Python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence:
    if char.lower() in vowels:
        sum += 1
print("Number of vowels:", sum)

