"""
Emails
Estimate: 25 minutes
Actual: 30 minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    prefix = email.split("@")[0]
    parts = prefix.replace(".", " ").split()
    return " ".join(parts).title()


if __name__ == "__main__":
    main()
