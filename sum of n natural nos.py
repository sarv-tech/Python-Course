# WAP to calculate the sum of first n natural numbers using for loop and range function.

num = int(input("Enter a number: "))
sum = 0
for n in range(1,num+1):
    sum += n
print("The sum of first",num,"natural numbers is:", sum)


# formula: sum = n(n+1)/2