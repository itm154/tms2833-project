from classes import Lecturer, Student
import ui
import auth


def main():
    user = None
    authenticated = False
    while not authenticated:
        choice = ui.select(
            "Choose to Register or Login", ["Register", "Log in", "Exit"]
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
        # Do things after authentication down here
        # Just an example
        print(f"Authenticated user email: {user.getUserEmail()}")


if __name__ == "__main__":
    main()
