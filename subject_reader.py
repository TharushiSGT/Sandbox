"""
CP1404/CP5632 - Practical 4
Subject Reader
"""
FILENAME = "subject_data.txt"

def load_data():
    """Read data from file."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subject_details(subjects):
    """Display the details for each subject."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:<12} and has {subject[2]:>3} students")

def main():
    """Load subject data and display it."""
    subjects = load_data()
    display_subject_details(subjects)

if __name__ == "__main__":
    main()