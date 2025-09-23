"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)

def main():
    """Main function for the temperature conversion program."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            try:
                celsius = float(input("Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"Result: {fahrenheit:.2f} F")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "F":
            try:
                fahrenheit = float(input("Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"Result: {celsius:.2f} C")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

if __name__ == "__main__":
    main()
