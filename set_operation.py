a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)         # Contain all the elements in a along with all the elements in b
print(c)

d = a.intersection(b)   # Contain only the elements that are in both a and b
print(d)

e = a.difference(b)    # Contain only the elements that are in a but not in b
print(e)

# Use Case: Sets are great for eliminating duplicate values.
