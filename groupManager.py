import os
import pickle

import auth
import ui
from classes import Group, Student

DATA_DIR = "data"


def createGroup(authenticatedUser: Student):
    # Prompt Group Details
    name = str(input("Please enter Group Name: "))
    id = ui.numeric_input("Please enter Group ID: ")

    newGroup = Group(name, id, authenticatedUser.getUserName())
    save_group(newGroup)
    print("Group created successfully.")
    joinGroup(authenticatedUser, newGroup.getGroupID())


def joinGroup(authenticatedUser: Student, groupID: int):
    # Loads the group and adds the student in it
    temp_group = load_group(groupID)

    if temp_group is None:
        print("Group not found.")
        return

    if authenticatedUser.getUserName() in temp_group.getMemberList():
        print(
            f"{authenticatedUser.getUserName()} is already a member of {temp_group.getGroupName()}."
        )
        return

    temp_group.addMember(authenticatedUser.getUserName())
    save_group(temp_group)
    # Loads the student and updates student joined group list
    authenticatedUser.joinGroup(groupID)
    auth.save_user(authenticatedUser)
    print(f"{authenticatedUser.getUserName()} successfully enrolled in group.")


def viewGroup(authenticatedUser: Student, groupID: int):
    temp_group = load_group(groupID)
    if temp_group is None:
        print("No groups available.")
        return

    if authenticatedUser.getUserName() not in temp_group.getMemberList():
        print("You are not a member of this group.")
        return

    print(f"Group Name: {temp_group.getGroupName()}")
    print(f"Leader: {temp_group.getGroupLeader()}")
    ui.display_list("Members", temp_group.getMemberList())
    print("Tasks: ")


def save_group(group: Group):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, f"group_{group.getGroupID()}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump(group, f)


def load_group(groupID: int) -> Group | None:
    file_path = os.path.join(DATA_DIR, f"group_{groupID}.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return None
