from .group import Group
from .user import User


class Report:
    def __init__(
        self,
        reportID: int,
        generatedDate: str,
        totalTasks: int,
        completedTasks: int,
        memberContribution: str,
    ):
        self.reportID = reportID
        self.generatedDate = generatedDate
        self.totalTasks = totalTasks
        self.completedTasks = completedTasks
        self.memberContribution = memberContribution

    def generateGroupSummary(self, group: Group):
        print(f"=== Group Summary Report (ReportID: {self.reportID}) ===")
        print(f"Generated Date: {self.generatedDate}")
        print(f"Group Name: {group.groupName}")
        print(f"Total Tasks: {len(group.tasks)}")

    def generateMemberReport(self, user: User):
        print(f"=== Member Report (ReportID: {self.reportID}) ===")
        print(f"Generated Date: {self.generatedDate}")
        print(f"Member: {user.userName}")
        print(f"Contribution: {self.memberContribution}")

    def calculateCompletionRate(self):
        if self.totalTasks == 0:
            rate = 0.0
        else:
            rate = (self.completedTasks / self.totalTasks) * 100
        print(f"Completion Rate: {rate:.2f}%")
        return rate

    def displayReport(self):
        print("=== Report Info ===")
        print(f"reportID: {self.reportID}")
        print(f"generatedDate: {self.generatedDate}")
        print(f"totalTasks: {self.totalTasks}")
        print(f"completedTasks: {self.completedTasks}")
        print(f"memberContribution: {self.memberContribution}")
