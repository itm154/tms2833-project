import data_manager
import ui_components
from classes import Student


def studentMenu(student: Student):
    while True:
        choice = ui_components.select(
            "Please Select An Action",
            [
                "Create Group",
                "Join Group",
                "View Group",
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
            case 3:  # View group
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
                        group_details = student.viewGroup(id_list[selected_group - 1])
                        if isinstance(group_details, dict):
                            print(f"Group Name: {group_details['group_name']}")
                            print(f"Leader: {group_details['leader']}")
                            ui_components.displayList(
                                "Members", group_details["members"]
                            )
                            # TODO: we need a component to display tasks
                            # print("Tasks: ")
                        else:
                            print(group_details)
            case 4:  # Display information
                ui_components.displayDict("My information", student.getInfo())

            case 5:  # Logging out
                break
