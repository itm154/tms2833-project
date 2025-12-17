import re
import getpass


def is_valid_email(email: str) -> bool:
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email) is not None


def email_inputfield() -> str:
    while True:
        email = input("Email: ")
        if is_valid_email(email):
            return email
        else:
            print("Error: Invalid email format. Please try again.")


def hidden_inputfield() -> str:
    password = getpass.getpass("Password: ")
    return password
