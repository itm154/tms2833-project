import auth
import ui
from classes import Group, Student


def studentMenu(authenticatedUser):
    while True:
        choice = ui.select(
            "Please Select An Action",
            ["Create Group", "Join Group", "View Group", "Log Out"],
        )
        match choice:
            case 1:
                createGroup(authenticatedUser)
                # Student Creates a Group
            case 2:
                pass
                # Student Joins a Group
            case 3:
                viewGroup(authenticatedUser)
                # Student Views an Existing Group
            case 4:
                # Logging out
                break


def createGroup(authenticatedUser: Student):
    # Prompt Group Details
    name = str(input("Please enter Group Name: "))
    id = ui.numeric_input("Please enter Group ID: ")

    newGroup = Group(name, id, authenticatedUser.getUserName())
    print("About to save")
    auth.save_group(newGroup)
    print("Group saved successfully.")
    authenticatedUser.joinGroup(newGroup.getGroupName())


def viewGroup(authenticatedUser: Student):
    print(authenticatedUser.getJoinedGroups())
