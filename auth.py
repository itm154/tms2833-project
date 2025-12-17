import pickle
import os
import ui
from classes import User, Student, Lecturer

DATA_DIR = "data"


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

    save_user(newUser)
    print(f"{newUser.getUserName()} was successfully registered.")
    return


def login():
    userName = str(input("Please insert your Username: "))
    userPassword = ui.hidden_input("Please enter your Password: ")

    user = load_user(userName)

    if user and user.getPassword() == userPassword:
        print(f"Welcome, {user.getUserName()}!")
        return user
        # Here you can add the logic for what happens after a successful login
    else:
        print("Invalid username or password.")


def save_user(user: User):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, f"{user.getUserName()}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump(user, f)


def load_user(username: str) -> User | None:
    file_path = os.path.join(DATA_DIR, f"{username}.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return None
