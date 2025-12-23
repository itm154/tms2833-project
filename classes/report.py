from datetime import datetime
from .user import User
from .group import Group


class Report:
    def __init__(self, report_id: int, group: Group):
        self.__report_id = report_id
        self.__generated_date = datetime.now()
        self.__group = group
        self.__total_tasks = len(self.__group.getTasks())
        self.__completed_tasks = 0

    def getReport(self) -> dict:
        return {
            "Report ID": self.__report_id,
            "Generated date": self.__generated_date,
            "Total tasks": self.__total_tasks,
            "Completed tasks": self.calculateCompletionRate(),
        }

    def generateMemberReport(self, user: User):
        print("=== Member Report ===")
        print(f"Report ID: {self.__report_id}")
        print(f"Generated Date: {self.__generated_date}")
        print(f"Member: {user.__user_name}")

    def calculateCompletionRate(self):
        if self.__total_tasks == 0:
            rate = 0.0
        else:
            rate = (self.__completed_tasks / self.__total_tasks) * 100

        print(f"Completion Rate: {rate:.2f}%")
        return rate

    def displayReport(self):
        print("=== Report Info ===")
        print(f"Report ID: {self.__report_id}")
        print(f"Generated Date: {self.__generated_date}")
        print(f"Total Tasks: {self.__total_tasks}")
        print(f"Completed Tasks: {self.__completed_tasks}")
