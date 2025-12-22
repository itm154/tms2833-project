import data_manager
import ui_components
from classes import Lecturer
from data_manager import group_manager


def lecturerMenu(lecturer: Lecturer):
    while True:
        choice = ui_components.select(
            "Please Select An Action",
            [
                "Generate group report",
                "View Group",
                "View My Information",
                "Log Out",
            ],
        )
        match choice:
            case 1:
                groups = group_manager.loadAllGroups()
                if not groups:
                    print("No groups available to generate report.")
                    continue

                group_names = [group.getGroupName() for group in groups]
                selected_group_index = ui_components.select(
                    "Select a group to generate report", group_names
                )
                selected_group = groups[selected_group_index - 1]

                report = lecturer.generateReport(selected_group.getGroupID(), 1)
                if isinstance(report, dict):
                    ui_components.displayDict(
                        f"{selected_group.getGroupName()} group report", report
                    )
                else:
                    print(report)
            case 2:
                pass
            case 3:
                pass
                ui_components.displayDict("My information", lecturer.getInfo())
            case 4:
                break
