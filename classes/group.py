class Group:
    def __init__(self, group_name: str, group_id: int, leader):
        self.__group_name = group_name
        self.__group_rn = group_id
        # Members should be only the leader after creation for now
        self.__members = []
        self.__leader = leader
        self.__tasks = []

    def getGroupName(self):
        return self.__group_name

    def getGroupID(self):
        return self.__group_rn

    def getGroupLeader(self):
        return self.__leader

    def getMemberList(self):
        return self.__members

    def addMember(self, new_member):
        self.__members.append(new_member)

    def addTasks(self, task):
        self.__tasks.append(task)

    def getTasks(self):
        return self.__tasks

    def getTaskById(self, task_id):
        for t in self.__tasks:
            if t.getTaskId() == task_id:
                return t
        return None

    def deleteTaskById(self, task_id: int) -> bool:
        for i, t in enumerate(self.__tasks):
            if t.getTaskId() == task_id:
                self.__tasks.pop(i)
                return True
        return False
