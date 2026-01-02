# Create a list Containing the table of 10

table = []

for i in range(1, 11):
    table.append(10*i)

    print(table)

print("\n")

# Shortcut
table = [10*i for i in range(1, 11)]
print(table)

print("\n")

# Square of 0 to 4
squared = [x**2 for x in range(5)]

print(squared)  

print("\n")

# Linear Search
nums = [1,2,3,10,4]
x = 10
idx = 0

for val in nums:
    if(val == x):
        print(f"{x} is found at index {idx}")
        break
    else:
        idx += 1
        
print("\n")

square = [i*i for i in range(6) if i % 2 != 0]
print(square)

print("\n")

nums = [-2, -3, 3, 4, -1, 7]

nums = [0 if val < 0 else val for val in nums]
print(nums)

print("\n")

words = ["python", "hello", "sarvesh"]

words = [val.upper() for val in words]
print(words)
