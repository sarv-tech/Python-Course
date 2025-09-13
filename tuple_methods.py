# Common Tuple methods :-

# 1) Count(x)
# Description: Return the number of times x appears in the tuple
# Example: (1, 2, 2, 3).count(2)
# Output: 2

# 2) index(x)
# Description: Returns the index of the first occurrence of x
# Example: (10, 20, 30).index(20)
# Output: 1

my_tuple = (1, 2, 2, 3, 4)
print(my_tuple.count(2)) 

print(my_tuple.index(3)) 

# Why Use Tuples?
# Faster than lists (since they are immutable)
# Used as dictionary keys (since they are hashable)
# Safe from unintended modifications