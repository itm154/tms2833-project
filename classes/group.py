from .task import Task


class Group:
    def __init__(self, group_name: str, group_id: int, leader):
        self.__group_name = group_name
        self.__group_id = group_id
        # Members should be only the leader after creation for now
        self.__members = []
        self.__leader = leader
        self.__tasks = []

    def addMember(self, new_member):
        self.__members.append(new_member)

    def addTasks(self, task: Task):
        self.__tasks.append(task)

    def deleteTaskById(self, task_id: int) -> bool:
        for i, t in enumerate(self.__tasks):
            if t.getTaskId() == task_id:
                self.__tasks.pop(i)
                return True
        return False

    def getGroupName(self) -> str:
        return self.__group_name

    def getGroupId(self) -> int:
        return self.__group_id

    def getGroupLeader(self) -> str:
        return self.__leader

    def getMemberList(self) -> list[str]:
        return self.__members

    def getTasks(self) -> list[Task]:
        return self.__tasks

    def getTaskById(self, task_id) -> Task | None:
        for t in self.__tasks:
            if t.getTaskId() == task_id:
                return t
        return None

    def getGroupInfo(self) -> dict:
        return {
            "Name": self.__group_name,
            "ID": self.__group_id,
            "Members": self.__members,
            "Leader": self.__leader,
        }
