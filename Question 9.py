# Q. Use a while loop to reverse a given number.

# 1st approach
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0 :
    digit = num % 10             # get last digit
    reversed_num = reversed_num * 10 + digit  # build reversed number
    num = num // 10              # remove last digit

print("Reversed number:", reversed_num)


# 2nd approach
num = int(input("Enter a number: "))

print(int(str(num)[::-1]))