# Temperature Converter in Python

# This program converts temperature values
# between Celsius, Fahrenheit, and Kelvin.


# Conversion Functions


# Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


# Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


# Celsius to Kelvin
def celsius_to_kelvin(c):
    return c + 273.15


# Kelvin to Celsius
def kelvin_to_celsius(k):
    return k - 273.15



# Main Program


def main():

    print("===================================")
    print("      TEMPERATURE CONVERTER")
    print("===================================")

    while True:

        # Display Menu
        print("\nChoose Conversion Type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Exit Program
        if choice == "5":
            print("\nThank you for using the Temperature Converter!")
            break

        # Validate choice
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select a valid option.")
            continue

        try:
            # Take temperature input
            temp = float(input("\nEnter temperature value: "))

        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

            # Perform Conversion

        if choice == "1":
            result = celsius_to_fahrenheit(temp)
            print(f"\n{temp}°C = {result:.2f}°F")

        elif choice == "2":
            result = fahrenheit_to_celsius(temp)
            print(f"\n{temp}°F = {result:.2f}°C")

        elif choice == "3":
            result = celsius_to_kelvin(temp)
            print(f"\n{temp}°C = {result:.2f}K")

        elif choice == "4":
            result = kelvin_to_celsius(temp)
            print(f"\n{temp}K = {result:.2f}°C")


main()
