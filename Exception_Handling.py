# Exception Handling :- In Exception Handling, basically we try to predict what are the possible errors that can occur in thr program and we try to manage them or try to handle the errors.
# try, except, catch, finally 

try:
    x = int(input("Enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")

except ValueError:
    print(f"Invalid input")

else:
    print(f"ans = {ans}")