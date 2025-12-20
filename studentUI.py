import groupManager
import ui
from classes import Student


def studentMenu(authenticatedUser: Student):
    while True:
        choice = ui.select(
            "Please Select An Action",
            ["Create Group", "Join Group", "View Group", "Log Out"],
        )
        match choice:
            case 1:
                # Student Creates a Group
                authenticatedUser.createGroup()

            case 2:
                # Student Joins a Group
                groupID = ui.numeric_input("Please enter the ID of the group: ")
                authenticatedUser.joinGroup(groupID)
            case 3:
                # Temporary lists used to fetch and display data
                groupNames = []
                id_list = []
                for groupID in authenticatedUser.getJoinedGroups():
                    tempGroup = groupManager.load_group(groupID)
                    if tempGroup:
                        groupNames.append(tempGroup.getGroupName())
                        id_list.append(groupID)
                selected_group = ui.select(
                    "Please Select the Group you wish to visit", groupNames
                )

                if id_list:
                    authenticatedUser.viewGroup(id_list[selected_group - 1])
            case 4:
                # Logging out
                break
