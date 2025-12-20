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
                groupManager.createGroup(authenticatedUser)

            case 2:
                # Student Joins a Group
                groupID = ui.numeric_input("Please enter the ID of the group: ")
                groupManager.joinGroup(authenticatedUser, groupID)
            case 3:
                # Temporary lists used to fetch and display data
                groupNames = []
                id_list = []
                for groupID in authenticatedUser.getJoinedGroups():
                    id_list.append(
                        groupID
                    )  # Put the list of IDs one by one into the list to match with user choice
                    tempGroup = groupManager.load_group(groupID)
                    groupNames.append(tempGroup.getGroupName())
                selected_group = ui.select(
                    "Please Select the Group you wish to visit", groupNames
                )

                groupManager.viewGroup(authenticatedUser, id_list[selected_group - 1])

                # This function was used to test group adding only, can change the logic of the function to it's intended use.
                # Student Views an Existing Group
            case 4:
                # Logging out
                break
