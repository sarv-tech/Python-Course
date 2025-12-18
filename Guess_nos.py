# Q. Let’s create a Number Guessing Game.
# Given  a secret number (already decided by you), write a program that asks the user to guess the number and prints:

# If the guess is above the secret number → "Too high"
# If the guess is below the secret number → "Too low"
# If the guess matches the secret number → "Correct! You guessed it"


secret_number = 32
guess_number = float(input("Enter Guess Number: "))

if(guess_number > secret_number):
    print("Too high")
elif(guess_number < secret_number):
    print("Too Low")
elif(guess_number == secret_number):
    print("Correct! You guessed it")
else:
    print("Guess Number is Invalid!")


print(guess_number)

