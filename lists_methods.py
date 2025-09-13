my_list = [1, 2, 3, 24, 73]
extra_list = [101, 200, 400, 1000, 132]
print(my_list)

print("\n")

my_list.append(4)   
print(my_list)

my_list.insert(1, 99)  
print(my_list)

my_list.remove(2)   
print(my_list)

my_list.pop(3)  
print(my_list)     

my_list.reverse()   
print(my_list)

my_list.sort()   
print(my_list)

my_list.extend(extra_list)
print(my_list)
