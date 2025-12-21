import ui_components
from data_manager import user_manager
from classes import Student, Lecturer


def register():
    # Fill general information
    user_name = str(input("Please insert your Username: "))
    user_email = ui_components.emailInput("Please enter your Email: ")
    user_password = ui_components.hiddenInput("Please enter your Password: ")

    user_type = ui_components.select(
        "Are you a Student or Lecturer?", ["Student", "Lecturer"]
    )

    # Register specific userType
    if user_type == 1:
        matric_number = ui_components.numericInput("Please enter your Matric Number: ")
        new_user = Student(user_name, matric_number, user_email, user_password, [])
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
        staff_id = ui_components.numericInput("Please enter your Staff ID: ")
        office = str(input("Please enter your Office location: "))
        faculty = faculty[
            ui_components.select("Please enter your Faculty: ", faculty) - 1
        ]
        course_id = input("Please enter your Course ID: ")
        new_user = Lecturer(
            user_name, staff_id, user_email, user_password, office, faculty, course_id
        )

    user_manager.saveUser(new_user)
    print(f"{new_user.getUserName()} was successfully registered.")
    return


def login():
    user_name = str(input("Please insert your Username: "))
    user_password = ui_components.hiddenInput("Please enter your Password: ")

    user = user_manager.loadUser(user_name)

    if user and user.getPassword() == user_password:
        print(f"Welcome, {user.getUserName()}!")
        return user
    else:
        print("Invalid username or password.")
