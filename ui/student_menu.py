import data_manager
import ui
import ui_components
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
            case 3:  #
                joined_groups = student.getJoinedGroups()
                if not joined_groups:
                    print("You are not part of any group.")
                else:
                    group_names = []
                    id_list = []
                    for group_id in joined_groups:
                        temp_group = data_manager.loadGroup(group_id)
                        if temp_group:
                            group_names.append(temp_group.getGroupName())
                            id_list.append(group_id)
                        else:
                            break
                    selected_index = ui_components.select(
                        "Please Select the Group you wish to visit", group_names
                    )
                    selected_group = data_manager.loadGroup(id_list[selected_index - 1])
                    if selected_group:
                        ui.taskMenu(selected_group)
            case 4:  # Display information
                ui_components.displayDict("My information", student.getInfo())

            case 5:  # Logging out
                break
