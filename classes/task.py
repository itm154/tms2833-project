from .user import User


class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        deadline: str,
        priority: int,
        status: str = "To Do",
        assignee: User | None = None,
    ):
        self.__task_id = task_id
        self.__title = title
        self.__description = description
        self.__deadline = deadline
        self.__priority = priority
        self.__status = status
        self.__assignee = assignee

    def createTask(self):
        print(f"Task '{self.__title}' created.")

    def updateStatus(self, new_status: str):
        self.__status = new_status
        print(f"Task status updated to '{self.__status}'.")

    def assignTo(self, user: User):
        self.__assignee = user
        print(f"Task assigned to {user}.")

    def editTask(
        self,
        new_title: str,
        new_desc: str,
        new_deadline: str,
        new_priority: int,
    ):
        self.__title = new_title
        self.__description = new_desc
        self.__deadline = new_deadline
        self.__priority = new_priority
        print("Task updated successfully.")

    def displayTaskInfo(self):
        print("=== Task Info ===")
        print(f"Task ID: {self.__task_id}")
        print(f"Title: {self.__title}")
        print(f"Description: {self.__description}")
        print(f"Deadline: {self.__deadline}")
        print(f"Priority: {self.__priority}")
        print(f"Status: {self.__status}")
        print(f"Assignee: {self.__assignee}")
