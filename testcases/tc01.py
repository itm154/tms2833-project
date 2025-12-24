from classes import Student
import ui_components


def tc01():
    print("TC-01: Create group")

    print("Creating new user...")
    new_user = Student("Tester", 123123, "test@gmail.com", "test", [])

    print("Creating group...")
    group, message = new_user.createGroup("Test Group", 67)

    if group is not None:
        print(message)
        ui_components.displayDict("Created Group", group.getGroupInfo())
    else:
        print("Test case failed! User failed to create group.")
        print("Message:" + message)
