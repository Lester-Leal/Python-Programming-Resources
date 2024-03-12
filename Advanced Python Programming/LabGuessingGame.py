import random

min_value = 1
max_value = 100
high_score = None  # Optional, initialize to None
low_score = None  # Optional, initialize to None

def play_game():
    secret_number = random.randint(min_value, max_value)
    guesses = 0

    print("Welcome to the Guessing Game!")
    print(f"I'm thinking of a number between {min_value} and {max_value}. Can you guess it?")

    while True:
        try:
            user_guess = int(input("Take a guess: "))
            guesses += 1

            if user_guess < secret_number:
                print("Too low. Try again!")
            elif user_guess > secret_number:
                print("Too high. Try again!")
            else:
                print(f"Congratulations! You guessed the number in {guesses} tries.")
                # Optional: Update statistics
                if high_score is None or guesses < high_score:
                    high_score = guesses
                if low_score is None or guesses > low_score:
                    low_score = guesses
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Optional: Display statistics
    if high_score is not None and low_score is not None:
        print(f"Your best game took {low_score} guesses.")
        print(f"It took you the longest in {high_score} guesses.")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != 'y':
        return

# Start the game
play_game()

print("Thanks for playing!")