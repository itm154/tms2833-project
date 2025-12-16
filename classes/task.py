from .user import User


class Task:
    def __init__(
        self,
        taskID: int,
        title: str,
        description: str,
        deadline: str,
        priority: int,
        status: str = "To Do",
        assignee: User | None = None,
    ):
        self.taskID = taskID
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.status = status
        self.assignee = assignee

    def createTask(self):
        print(f"Task '{self.title}' created.")

    def updateStatus(self, newStatus: str):
        self.status = newStatus
        print(f"Task status updated to '{self.status}'.")

    def assignTo(self, user: User):
        self.assignee = user
        print(f"Task assigned to {user}.")

    def editTask(self, newTitle, newDesc, newDeadline, newPriority):
        self.title = newTitle
        self.description = newDesc
        self.deadline = newDeadline
        self.priority = newPriority
        print("Task updated successfully.")

    def displayTaskInfo(self):
        print("=== Task Info ===")
        print(f"taskID: {self.taskID}")
        print(f"title: {self.title}")
        print(f"description: {self.description}")
        print(f"deadline: {self.deadline}")
        print(f"priority: {self.priority}")
        print(f"status: {self.status}")
        print(f"assignee: {self.assignee}")
