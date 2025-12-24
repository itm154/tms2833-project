import ui_components
from .group_menu import groupMenu
from classes import Lecturer
from data_manager import group_manager


def lecturerMenu(lecturer: Lecturer):
    while True:
        choice = ui_components.select(
            "Please Select An Action",
            [
                "Generate Group report",
                "Group dashboard",
                "View My Information",
                "Log Out",
            ],
        )
        match choice:
            case 1:  # Generate group report
                selected_group = ui_components.selectGroup("Select a group")

                if selected_group:
                    report = lecturer.generateReport(selected_group.getGroupId())
                    if isinstance(report, dict):
                        ui_components.displayDict(
                            f"{selected_group.getGroupName()} group report", report
                        )
                    else:
                        print(report)
            case 2:  # View group
                selected_group = ui_components.selectGroup(
                    "Please Select the Group you wish to operate in"
                )
                if selected_group:
                    groupMenu(selected_group)
            case 3:  # View my information
                pass
                ui_components.displayDict("My information", lecturer.getInfo())
            case 4:
                break
