"""
State Names
Estimate: 15 minutes
Actual: 12 minutes
"""

STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}


def main():
    print("Welcome to the state names lookup program.")
    # Print all abbreviations and state names
    for short_name, full_name in STATE_NAMES.items():
        print(f"{short_name:3} is {full_name}")

    state_code = input("\nEnter short state: ").strip().upper()
    while state_code != "":
        try:
            print(f"{state_code} is {STATE_NAMES[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip().upper()


if __name__ == "__main__":
    main()
