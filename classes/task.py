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
        self.__taskID = taskID
        self.__title = title
        self.__description = description
        self.__deadline = deadline
        self.__priority = priority
        self.__status = status
        self.__assignee = assignee

    def createTask(self):
        print(f"Task '{self.__title}' created.")

    def updateStatus(self, newStatus: str):
        self.__status = newStatus
        print(f"Task status updated to '{self.__status}'.")

    def assignTo(self, user: User):
        self.__assignee = user
        print(f"Task assigned to {user}.")

    def editTask(self, newTitle, newDesc, newDeadline, newPriority):
        self.__title = newTitle
        self.__description = newDesc
        self.__deadline = newDeadline
        self.__priority = newPriority
        print("Task updated successfully.")

    def displayTaskInfo(self):
        print("=== Task Info ===")
        print(f"Task ID: {self.__taskID}")
        print(f"Title: {self.__title}")
        print(f"Description: {self.__description}")
        print(f"Deadline: {self.__deadline}")
        print(f"Priority: {self.__priority}")
        print(f"Status: {self.__status}")
        print(f"Assignee: {self.__assignee}")
