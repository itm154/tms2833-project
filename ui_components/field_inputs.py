import getpass
import re
from datetime import date, datetime


# User Interface Components for Field Input Validation
# Implemented by: Muhammad Ashrul Fahmi (102725)
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


def dateInput(prompt: str) -> date:
    while True:
        try:
            date = str(input(prompt))
            return datetime.strptime(date, "%d/%m/%Y").date()
        except ValueError:
            print("Error: Invalid date or format. Please follow the format dd/mm/yyyy")
