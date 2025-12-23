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
        self.__priority = min(priority, 5)  # Since numeric input is unbounded.
        self.__status = status
        self.__assignee = assignee

    def updateStatus(self, new_status: str):
        self.__status = new_status
        return f"Task status updated to '{self.__status}'."

    def assignTo(self, user: str):
        self.__assignee = user
        return f"Task assigned to {user}."

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

    def getTaskId(self) -> int:
        return self.__task_id

    def getInfo(self) -> dict:
        return {
            "Task ID": self.__task_id,
            "Title": self.__title,
            "Description": self.__description,
            "Deadline": self.__deadline,
            "Priority": self.__priority,
            "Status": self.__status,
            "Assignee": self.__assignee,
        }
