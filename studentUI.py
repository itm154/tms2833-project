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
                groupManager.createGroup(authenticatedUser)
                # Student Creates a Group
            case 2:
                pass
                # Student Joins a Group
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

                groupManager.viewGroup(id_list[selected_group - 1])

                # This function was used to test group adding only, can change the logic of the function to it's intended use.
                # Student Views an Existing Group
            case 4:
                # Logging out
                break
