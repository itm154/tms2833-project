from .user import User
from .group import Group


class Report:
    def __init__(
        self,
        reportID: int,
        generatedDate: str,
        totalTasks: int,
        completedTasks: int,
        memberContribution: str,
    ):
        self.__reportID = reportID
        self.__generatedDate = generatedDate
        self.__totalTasks = totalTasks
        self.__completedTasks = completedTasks
        self.__memberContribution = memberContribution

    def generateGroupSummary(self, group: Group):
        print("=== Group Summary Report ===")
        print(f"Report ID: {self.__reportID}")
        print(f"Generated Date: {self.__generatedDate}")
        print(f"Group Name: {group.__groupName}")
        print(f"Total Tasks: {len(group.__tasks)}")

    def generateMemberReport(self, user: User):
        print("=== Member Report ===")
        print(f"Report ID: {self.__reportID}")
        print(f"Generated Date: {self.__generatedDate}")
        print(f"Member: {user.__userName}")
        print(f"Contribution: {self.__memberContribution}")

    def calculateCompletionRate(self):
        if self.__totalTasks == 0:
            rate = 0.0
        else:
            rate = (self.__completedTasks / self.__totalTasks) * 100

        print(f"Completion Rate: {rate:.2f}%")
        return rate

    def displayReport(self):
        print("=== Report Info ===")
        print(f"Report ID: {self.__reportID}")
        print(f"Generated Date: {self.__generatedDate}")
        print(f"Total Tasks: {self.__totalTasks}")
        print(f"Completed Tasks: {self.__completedTasks}")
        print(f"Member Contribution: {self.__memberContribution}")
