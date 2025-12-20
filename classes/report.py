from .user import User
from .group import Group


class Report:
    def __init__(
        self,
        report_id: int,
        generated_date: str,
        total_tasks: int,
        completed_tasks: int,
        member_contribution: str,
    ):
        self.__report_id = report_id
        self.__generated_date = generated_date
        self.__total_tasks = total_tasks
        self.__completed_tasks = completed_tasks
        self.__member_contribution = member_contribution

    def generateGroupSummary(self, group: Group):
        print("=== Group Summary Report ===")
        print(f"Report ID: {self.__report_id}")
        print(f"Generated Date: {self.__generated_date}")
        print(f"Group Name: {group.__group_name}")
        print(f"Total Tasks: {len(group.__tasks)}")

    def generateMemberReport(self, user: User):
        print("=== Member Report ===")
        print(f"Report ID: {self.__report_id}")
        print(f"Generated Date: {self.__generated_date}")
        print(f"Member: {user.__user_name}")
        print(f"Contribution: {self.__member_contribution}")

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
        print(f"Member Contribution: {self.__member_contribution}")
