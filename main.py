from classes import Lecturer, Student
import ui
import auth


# Flow of app
# 1. Login (Please take over for auth regisering issues)
# 2. Implement different UIs for different Users


# Function to register a New User
def register():
    # Fill general information
    userName = str(input("Please insert your Username: "))
    userEmail = ui.email_input("Please enter your Email: ")
    userPassword = ui.hidden_input("Please enter your Password: ")

    userType = ui.select("Are you a Student or Lecturer?", ["Student", "Lecturer"])

    # Register specific userType
    if userType == 1:
        matricNumber = ui.numeric_input("Please enter your Matric Number: ")
        newUser = Student(userName, matricNumber, userEmail, userPassword, [])
    else:
        faculty = [
            "FEB",
            "FENG",
            "FACA",
            "FCSHD",
            "FMHS",
            "FSSH",
            "FRST",
            "FCSIT",
            "FELC",
            "FBE",
        ]
        staffID = ui.numeric_input("Please enter your Staff ID: ")
        office = str(input("Please enter your Office location: "))
        faculty = faculty[ui.select("Please enter your Faculty: ", faculty) - 1]
        courseID = input("Please enter your Course ID: ")
        newUser = Lecturer(
            userName, staffID, userEmail, userPassword, office, faculty, courseID
        )

    auth.save_user(newUser)
    print(f"{newUser.getUserName()} was successfully registered.")
    return


def login():
    userName = str(input("Please insert your Username: "))
    userPassword = ui.hidden_input("Please enter your Password: ")

    user = auth.load_user(userName)

    if user and user.getPassword() == userPassword:
        print(f"Welcome, {user.getUserName()}!")
        # Here you can add the logic for what happens after a successful login
    else:
        print("Invalid username or password.")


def main():
    while True:
        choice = ui.select(
            "Choose to Register or Login", ["Register", "Log in", "Exit"]
        )
        match choice:
            case 1:
                register()
            case 2:
                login()
            case 3:
                return


if __name__ == "__main__":
    main()
