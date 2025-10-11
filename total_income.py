"""
CP1404/CP5632 - Practical
Starter code for cumulative total income program
"""

def print_income_report(incomes):
    """Print a formatted income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month_index, income in enumerate(incomes):
        total += income
        print(f"Month {month_index + 1:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)

if __name__ == "__main__":
    main()