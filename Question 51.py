# Q. Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.


def fibonacci(n, a=0, b=1):      # a and b are the first two Fibonacci numbers
    if n <= 0:                   # base case for recursion to stop the function when n is 0 negative  
        return
    print(a, end=' ')             # print the current Fibonacci number 
    fibonacci(n-1, b, a+b)        # recursive call with updated values 

n = int(input("Enter the number of Fibonacci numbers to print: "))
fibonacci(n)
