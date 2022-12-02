# Number Guessing Game - Guess a number between 1 and 20
# Author: Lester Leal

import random

# define the main function
def main():
    # generate a random number between 1 and 20
    number = random.randrange(1, 21)

    # initialize the guess variable
    guess = 0

    # initialize the number of guesses
    numGuesses = 0

    # prompt the user to guess the number
    print("I am thinking of a number between 1 and 20.")

    # loop until the user guesses the number
    while guess != number:
        # get the user's guess
        guess = int(input("Take a guess: "))

        # increment the number of guesses
        numGuesses += 1

        # compare the user's guess to the number
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")

    # display the number of guesses
    print("Good job! You guessed my number in", numGuesses, "guesses!")

main()