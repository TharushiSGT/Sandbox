"""
Wimbledon
Estimate: 35 minutes
Actual: 40 minutes
"""

FILENAME = r"C:\Users\ADMIN\Downloads\wimbledon (1).csv"



def main():
    data = load_data(FILENAME)
    champion_to_wins, countries = process_data(data)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read the Wimbledon data file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        data = [line.strip().split(",") for line in in_file]
    return data


def process_data(data):
    """Process the data into a dictionary of champions and their win counts, and a set of countries."""
    champion_to_wins = {}
    countries = set()
    for record in data:
        champion = record[2]
        country = record[1]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
        countries.add(country)
    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display the results neatly."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
