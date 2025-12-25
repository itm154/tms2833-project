from datetime import datetime

from .group import Group


# Class: Report
# Implemented by: Hii Chiong Hing (104347)
class Report:
    def __init__(self, report_id: int, group: Group):
        self.__report_id = report_id
        self.__generated_date = datetime.now()
        self.__group = group
        self.__total_tasks = len(self.__group.getTasks())
        self.__completed_tasks = sum(
            1 for task in self.__group.getTasks() if task.getStatus() == "Completed"
        )

    def getReport(self) -> dict:
        return {
            "Report ID": self.__report_id,
            "Generated date": self.__generated_date,
            "Total tasks": self.__total_tasks,
            "Completed tasks": self.__completed_tasks,
            "Completion rate": self.__calculateCompletionRate(),
        }

    def __calculateCompletionRate(self) -> float:
        if self.__total_tasks == 0:
            rate = 0.0
        else:
            rate = (self.__completed_tasks / self.__total_tasks) * 100

        print(f"Completion Rate: {rate:.2f}%")
        return rate

    def getTotalTasks(self) -> int:
        return self.__total_tasks
