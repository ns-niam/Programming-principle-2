# Thirteen exercise: write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.  
# This is how it should work when run in a terminal:

import random

def secret_number():
    print("Hello. What is your name?")
    name = input()
    secret_number = random.randint(1, 20) # Please choose a random number's code:
    print("I am thinking of a number between 1 and 20.")
    guesses_taken = 0

    while True: # This loop continues until the number is correct, stopping in the loop if the number is incorrect.
        guess = int(input("Try to guess the number I am thinking of: ")) # The user enters a number
        guesses_taken += 1 # We add numbers to our attempts
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print("Well done! You guessed the number.")
            break  

secret_number()
