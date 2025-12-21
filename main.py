import user_auth
import ui_components
import ui
from classes import Lecturer, Student


def main():
    user = None
    authenticated = False
    while not authenticated:
        choice = ui_components.select(
            "Choose to Register or Login",
            ["Register", "Log in", "Exit"],
        )
        match choice:
            case 1:
                user_auth.register()
            case 2:
                user = user_auth.login()
                if user:
                    authenticated = True
            case 3:
                return

    if user:
        if isinstance(user, Student):
            ui.studentMenu(user)
        elif isinstance(user, Lecturer):
            pass
        else:
            pass

        authenticated = False


if __name__ == "__main__":
    main()
