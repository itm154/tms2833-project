import data_manager
import ui_components
from classes import Lecturer


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
                pass
            case 2:
                pass
            case 3:
                pass
                ui_components.displayDict("My information", lecturer.getInfo())
            case 4:
                break
