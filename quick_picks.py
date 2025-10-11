"""
CP1404/CP5632 - Practical 4
"Quick Pick" Lottery Ticket Generator
"""
import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    """Generate and display a user-defined number of quick picks."""
    num_quick_picks = int(input("How many quick picks? "))

    for i in range(num_quick_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_PICK:
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if random_number not in quick_pick:
                quick_pick.append(random_number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

if __name__ == "__main__":
    main()