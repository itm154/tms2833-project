import re
import getpass


def is_valid_email(email: str) -> bool:
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email) is not None


def email_input(prompt: str) -> str:
    while True:
        email = input(prompt)
        if is_valid_email(email):
            return email
        else:
            print("Error: Invalid email format. Please try again.")


def hidden_input(prompt: str) -> str:
    password = getpass.getpass(prompt)
    return password


def numeric_input(prompt: str) -> int:
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
