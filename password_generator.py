# Password Generator in Python

# This program generates a random secure password
# based on the user-defined password length.

# Import Required Modules

import random
import string



# Function to Generate Password


def generate_password(length):

    # Combine all character types
    characters = (
        string.ascii_letters +   # A-Z and a-z
        string.digits +          # 0-9
        string.punctuation       # Special symbols
    )

    # Generate random password
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

# Main Program


def main():

    print("===================================")
    print("      PASSWORD GENERATOR")
    print("===================================")

    while True:

        try:
            # Take password length input
            length = int(input("\nEnter password length: "))

            # Validate length
            if length <= 0:
                print("Password length must be greater than 0.")
                continue

            # Generate password
            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Ask user if they want another password
        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the Password Generator!")
            break

main()
