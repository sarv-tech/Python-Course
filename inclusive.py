# Q. WAP to Print All Even Numbers Between Two Integers inclusive a and b

def print_even_numbers(a, b):
    # Ensure a is smaller than b
    if a > b:
        a, b = b, a
    # Loop through the range from a to b (inclusive)
    for num in range(a, b + 1):
        if num % 2 == 0:  # Check if number is even
            print(num, end=' ')
    print()  


print_even_numbers(3, 12)
