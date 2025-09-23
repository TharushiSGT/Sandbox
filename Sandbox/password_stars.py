# Set the minimum length for the password
MIN_LENGTH = 8

def get_password():
    """Prompts for a password and repeats until it's long enough."""
    while True:
        password = input(f"Enter a password (min. {MIN_LENGTH} characters): ")
        if len(password) >= MIN_LENGTH:
            return password
        else:
            print("Password too short. Try again.")

def print_asterisks(password):
    """Prints an asterisk for each character in the password."""
    print("*" * len(password))

def main():
    """Main function to run the program."""
    user_password = get_password()
    print("\nPassword accepted.")
    print_asterisks(user_password)

if __name__ == "__main__":
    main()
