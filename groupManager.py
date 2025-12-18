import auth
import ui
from classes import Group, Student


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
