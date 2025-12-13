class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        deadline,
        priority: int,
        assignee=None,
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.status = "To Do"
        self.assignee = assignee

    def createTask(self):
        print(f"Task '{self.title}' created.")

    def updateStatus(self, new_status: str):
        self.status = new_status
        print(f"Task status updated to '{self.status}'.")

    def assignTo(self, user):
        self.assignee = user
        print(f"Task assigned to {user}.")

    def editTask(self, new_title, new_desc, new_deadline, new_priority):
        self.title = new_title
        self.description = new_desc
        self.deadline = new_deadline
        self.priority = new_priority
        print("Task updated successfully.")

    def displayTaskInfo(self):
        print("=== Task Info ===")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Deadline: {self.deadline}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print(f"Assignee: {self.assignee}")
