import data_manager
import ui_components
from classes import Student


def studentMenu(student: Student):
    while True:
        choice = ui_components.select(
            "Please Select An Action",
            ["Create Group", "Join Group", "View Group", "Log Out"],
        )
        match choice:
            case 1:
                # Student Creates a Group
                name = str(input("Please enter Group Name: "))
                id = ui_components.numericInput("Please enter Group ID: ")
                student.createGroup(name, id)

            case 2:
                # Student Joins a Group
                group_id = ui_components.numericInput(
                    "Please enter the ID of the group: "
                )
                student.joinGroup(group_id)
            case 3:
                joined_groups = student.getJoinedGroups()
                if not joined_groups:
                    print("You are not part of any group.")
                else:
                    # Temporary lists used to fetch and display data
                    group_names = []
                    id_list = []
                    for group_id in joined_groups:
                        temp_group = data_manager.loadGroup(group_id)
                        if temp_group:
                            group_names.append(temp_group.getGroupName())
                            id_list.append(group_id)
                    selected_group = ui_components.select(
                        "Please Select the Group you wish to visit", group_names
                    )

                    if id_list:
                        student.viewGroup(id_list[selected_group - 1])
            case 4:
                # Logging out
                break
