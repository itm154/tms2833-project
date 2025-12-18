import auth
import studentUI
import ui
from classes import Lecturer, Student


def main():
    user = None
    authenticated = False
    while not authenticated:
        choice = ui.select(
            "Choose to Register or Login",
            ["Register", "Log in as Student", "Exit"],
        )
        match choice:
            case 1:
                auth.register()
            case 2:
                user = auth.login()
                if user:
                    authenticated = True
            case 3:
                return

    if user:
        if isinstance(user, Student):
            studentUI.studentMenu(user)
        elif isinstance(user, Lecturer):
            pass
        else:
            pass
        # Do things after authentication down here
        # Just an example
        authenticated = False
        print(f"Authenticated user email: {user.getUserEmail()}")


if __name__ == "__main__":
    main()
