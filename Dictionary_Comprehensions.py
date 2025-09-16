# Dictionary of the multiplication table of 5 using dictionary comprehension
table_of_5 = {i: i * 5 for i in range(1, 11)}

print(table_of_5)

# Dictionary of squares of numbers from 1 to 5 using dictionary comprehension
squares = {x: x**2 for x in range(5)}

print(squares)  


# Data Structure	 Features	                         Best For
# List	            Ordered, Mutable	       Storing sequences, dynamic data
# Tuple	            Ordered, Immutable	       Fixed collections, dictionary keys
# Set	            Unordered, Unique	       Removing duplicates, set operations
# Dictionary	    Key-Value Pairs	            Fast lookups, structured data