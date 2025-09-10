# Lambda functions are anonymous, inline functions.

square = lambda x : x*x

print(square(3))

'''
As good as writing
def square(x): 
    return x*x
'''

sum = lambda x,y : x + y

print(sum(3,43))
'''
As good as writing
def sum(x,y): 
    return x+y
'''