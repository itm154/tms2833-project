from classes import Lecturer, Student
import ui

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
        newStudent = Student(userName, matricNumber, userEmail, userPassword, [])
        print(f"{newStudent.getUserName()} was successfully registered.")
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
        newLecturer = Lecturer(
            userName, staffID, userEmail, userPassword, office, faculty, courseID
        )
        print(f"{newLecturer.getUserName()} was successfully registered.")
    return


def main():
    while True:
        choice = ui.select(
            "Choose to Register or Login", ["Register", "Log in", "Exit"]
        )
        match choice:
            case 1:
                register()
            case 2:
                # login()
                pass
            case 3:
                return


if __name__ == "__main__":
    main()
