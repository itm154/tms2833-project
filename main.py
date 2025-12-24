import argparse

import testcases
import ui
import ui_components
import user_auth
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
            ui.lecturerMenu(user)
        else:
            pass

        authenticated = False


def runTests():
    testcases.tc01()
    testcases.tc02()
    testcases.tc03()
    testcases.tc04()
    testcases.tc05()


if __name__ == "__main__":
    # Run either automated test or the program based on command line flags
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument("--test", action="store_true", help="Run automated testing")
    args = parser.parse_args()
    if args.test:
        runTests()
    else:
        main()
