# Python Calculator

A simple command-line calculator application built using Python.

## Features
- Addition
- Subtraction
- Multiplication
- Division
- Input validation
- Loop-based menu system


## Technologies Used
- Python

## How to Run
Run the calculator.py file using Python.

## Purpose
To practice Python functions, conditions, loops, and modular programming.

#Code for Calculator

# ==========================================
# Simple Calculator Application in Python
# ==========================================

# This program performs basic arithmetic operations:
# Addition, Subtraction, Multiplication, and Division

# --------------------------------------------
# Function Definitions

# Addition Function
def add(a, b):
    return a + b


# Subtraction Function
def subtract(a, b):
    return a - b


# Multiplication Function
def multiply(a, b):
    return a * b


# Division Function
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# ------------------------------------------
# Main Calculator Program
# ------------------------------------------

def calculator():

    print("===================================")
    print("      PYTHON CALCULATOR APP")
    print("===================================")

    while True:

        # Display Menu
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Exit Condition
        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        # Validate Choice
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select a valid option.")
            continue

        # Taking User Input
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        # Perform Operations
        if choice == "1":
            result = add(num1, num2)
            operation = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operation = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operation = "*"

        elif choice == "4":
            result = divide(num1, num2)
            operation = "/"

        # Display Result
        print("\n===================================")
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("===================================")


calculator()
