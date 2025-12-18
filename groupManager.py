import os
import pickle

import ui
from classes import Group, Student

DATA_DIR = "data"


def createGroup(authenticatedUser: Student):
    # Prompt Group Details
    name = str(input("Please enter Group Name: "))
    id = ui.numeric_input("Please enter Group ID: ")

    newGroup = Group(name, id, authenticatedUser.getUserName())
    save_group(newGroup)
    authenticatedUser.joinGroup(
        newGroup.getGroupID()
    )  # This is likely per session only, need update student data
    print("Group saved successfully.")


def viewGroup(groupID):
    tempGroup = load_group(groupID)
    print(f"{tempGroup.getGroupName()} was loaded.")
    return tempGroup
    # Can call task menu here and proceed with tasks handling


def save_group(group: Group):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, f"group_{group.getGroupID()}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump(group, f)


def load_group(groupID) -> Group | None:
    file_path = os.path.join(DATA_DIR, f"group_{groupID}.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return None
