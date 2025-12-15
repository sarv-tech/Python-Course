# Q. Given a list of integers compute the average of all numbers in the list


l = [1, 2, 3, 4]
sum = 0

for n in l:
    sum += n

average = sum / len(l)
print("Average is: ", average)

