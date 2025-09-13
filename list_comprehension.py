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