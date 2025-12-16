from ui import display_list, select

# Flow of app
# 1. Login (Please take over for auth regisering issues)
# 2. Implement different UIs for different Users


def loginPage():
    title_list = []
    display_list("Welcome to Our App!", title_list)
    login_choice = ["Register As User", "Log in", "Exit"]
    choice = select("Please select a choice", login_choice)
    print(f"You have selected {choice}")  # Testing purposes only


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
    loginChoice = loginPage()  
    if loginChoice == 1:
        # Register a New User
        # Register user
    elif loginChoice == 2:
        # Login Successful
        # if login == "student"
        #       studentMenu()
        # else:
        #   lecturerMenu()
            
    else:
        return 0
        #Exits the program.
        #No error handling is required here because it is already validated with select function earlier in loginPage()

main()
