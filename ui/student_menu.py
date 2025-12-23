import data_manager
import ui_components
from .group_menu import groupMenu
from classes import Student


def studentMenu(student: Student):
    while True:
        choice = ui_components.select(
            "Please Select An Action",
            [
                "Create Group",
                "Join Group",
                "Go to Group dashboard",
                "View My Information",
                "Log Out",
            ],
        )
        match choice:
            case 1:  # Create group
                name = str(input("Please enter Group Name: "))
                id = ui_components.numericInput("Please enter Group ID: ")
                new_group, message = student.createGroup(name, id)
                if new_group:
                    data_manager.saveGroup(new_group)
                    data_manager.saveUser(student)
                print(message)

            case 2:  # Join group
                group_id = ui_components.numericInput(
                    "Please enter the ID of the group: "
                )
                group, message = student.joinGroup(group_id)
                if group:
                    data_manager.saveGroup(group)
                    data_manager.saveUser(student)
                print(message)
            case 3:  # Go to Group dashboard
                joined_groups_ids = student.getJoinedGroups()
                if not joined_groups_ids:
                    print("You are not part of any group.")
                else:
                    joined_groups = [
                        group
                        for group_id in joined_groups_ids
                        if (group := data_manager.loadGroup(group_id))
                    ]
                    selected_group = ui_components.selectGroup(
                        "Please Select the Group you wish to operate in", joined_groups
                    )
                    if selected_group:
                        groupMenu(selected_group)
            case 4:  # Display information
                ui_components.displayDict("My information", student.getInfo())

            case 5:  # Logging out
                break
