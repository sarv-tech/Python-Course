# Q. Create two sets:
# a = {1, 2, 3}
# b = {3, 4, 5}

# Find their:
# Union
# Intersection
# Difference (a - b)


a = {1, 2, 3}
b = {3, 4, 5}

# Union
result = a.union(b)  # All unique elements from both a and b
print(result)

# Intersection
result = a.intersection(b)  # Elements common to both a and b
print(result)

# Difference
result = a.difference(b)  # Elements in a but not in b
print(result)