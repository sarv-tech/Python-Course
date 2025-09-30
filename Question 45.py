# Q. Write a lambda function that adds two numbers and test it.

add = lambda x,y : x + y
print(add(5, 3))




# Q. Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

squared_numbers = lambda x: x**2
numbers = [1, 2, 3, 4, 5]

print(list(map(squared_numbers, numbers)))   