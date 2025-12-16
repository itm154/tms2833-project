from ui import display_list, select

# Flow of app
# 1. Login (Please take over for auth regisering issues)
# 2. Implement different UIs for different Users


def loginPage():
    title_list = []
    display_list("Welcome to Our App!", title_list)
    login_choice = ["Register As User", "Log in", "Log Out"]
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
    loginPage()  # Implement Login Page so far


main()
