"""
CP1404/CP5632 - Practical
"""

import random

def determine_score_status(score):
    """
    Determine the status of a score and return the result as a string.
    This function does NOT print anything, adhering to the Single Responsibility Principle.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    """
    Main function to get a score from the user, determine its status,
    and also test the function with a random score.
    """
    # Part 1
    try:
        score = float(input("Enter score: "))
        result = determine_score_status(score)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a number.")

    print("---")

    # Part 2:
    random_score = random.randint(0, 100)
    print(f"Random score is: {random_score}")
    random_result = determine_score_status(random_score)
    print(random_result)


if __name__ == "__main__":
    main()
