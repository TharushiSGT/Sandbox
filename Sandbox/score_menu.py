def get_valid_score():
    """Gets a valid score (0-100 inclusive) from the user."""
    score = -1
    while not 0 <= score <= 100:
        try:
            score = float(input("Enter a score (0-100): "))
            if not 0 <= score <= 100:
                print("Invalid score. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return score


def get_score_result(score):
    """Determines the result of a score based on a fixed scale."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Prints a line of stars equal to the score."""
    print("*" * int(score))


def main():
    """A menu-driven program for score handling."""
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

    current_score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            current_score = get_valid_score()
        elif choice == "P":
            result = get_score_result(current_score)
            print(f"The result for a score of {current_score} is: {result}")
        elif choice == "S":
            print_stars(current_score)
        else:
            print("Invalid option. Please try again.")

        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye!")


if __name__ == "__main__":
    main()
