import re
import getpass


def isValidEmail(email: str) -> bool:
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email) is not None


def emailInput(prompt: str) -> str:
    while True:
        email = input(prompt)
        if isValidEmail(email):
            return email
        else:
            print("Error: Invalid email format. Please try again.")


def hiddenInput(prompt: str) -> str:
    password = getpass.getpass(prompt)
    return password


def numericInput(prompt: str) -> int:
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
