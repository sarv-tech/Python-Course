# Q. Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers


tup = (1, 2, 3, 4, 5, 6, 7, 8)
even_list = []
odd_list =  []

for num in tup:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

even_tup = tuple(even_list)
odd_tup = tuple(odd_list)    # list can be converted into tuple because it is mutable

print("Even tuple is: ", even_tup)  

print("odd tuple is: ", odd_tup)
