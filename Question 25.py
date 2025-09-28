# Using format(), create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.

x = 'john'
y = "25"
result = "My name is " + x + " and I am " + y + " years old."
print(result.format(x, y))

# Do the same using f-strings.
result = f'My name is {x} and I am {y} years old.'
print(result)