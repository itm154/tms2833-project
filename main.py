from classes import Lecturer, Student
from ui import display_list, select

# Flow of app
# 1. Login (Please take over for auth regisering issues)
# 2. Implement different UIs for different Users


# Function to register a New User
def registerUser():
    # Prompt user to choose account type
    choices = ["Student", "Lecturer"]
    # Need discussion on implementation of select
    prompt = 1
    # select("Are you a Student or Lecturer?", choices)
    # Fill general information (Super-class attribute)
    userName = str(input("Please insert your username: "))
    userID = int(input("Please enter your userID: "))
    userEmail = str(input("Please enter your email"))
    userPassword = str(input("Please enter your desired password: "))
    # If student is chosen
    if prompt == 1:
        # Subclass specific info (which is none because students don't join groups by default)
        newStudent = Student(userName, userID, userEmail, userPassword, [])
        print(f"{newStudent} was registered.")
    else:
        # If lecturer is chosen
        # Subclass specific info
        office = str(input("Please enter your office: "))
        faculty = str(input("Please enter your faculty: "))
        courseID = int("Please enter ID of the course you teach: ")
        newLecturer = Lecturer(
            userName, userID, userEmail, userPassword, office, faculty, courseID
        )
        print(f"{newLecturer} was registered.")


def mainMenuOptions():
    pass


def taskOptions():
    choice_list = [
        "Create Task",
        "Update Status",
        "Assign Task",
        "Edit Task",
        "Display Task Info",
    ]
    select("Please pick a choice", choice_list)


def main():
    # First Page => Login Page
    # Login Page decides first action of the user.
    choice = select(
        "Choose to Register or Login", ["Register As User", "Log in", "Exit"]
    )
    print(choice)
    match choice:
        case 1:
            registerUser()
        case 2:
            # login()
            pass
        case 3:
            return


if __name__ == "__main__":
    main()
