# Number Guessing Game in Python

# This program generates a random number and asks the user to guess it.


# Import Required Module

import random


# Main Game Function

def number_guessing_game():

    print("===================================")
    print("      NUMBER GUESSING GAME")
    print("===================================")

    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Counter for number of attempts
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess the number!")


    # Game Loop


    while True:

        try:
            # Taking user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue


        # Check User Guess


        if guess < secret_number:
            print("Too low! Try a bigger number.")

        elif guess > secret_number:
            print("Too high! Try a smaller number.")

        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number {secret_number} correctly.")
            print(f"Total attempts: {attempts}")
            break



# Play Again Feature


while True:

    # Start Game
    number_guessing_game()

    # Ask user to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing!")
        break
