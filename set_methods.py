s = {34, 23, 1, 3, 22}

print(s)

s.add(100)
s.remove(3)
# s.remove(1000)  # This will raise a KeyError if 1000 is not in the set
s.discard(1000)  # This will not raise an error if 1000 is not in the set
print(s)