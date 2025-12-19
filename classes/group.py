class Group:
    def __init__(self, groupName: str, groupId: int, leader):
        self.__groupName = groupName
        self.__groupId = groupId
        # Members should be only the leader after creation for now
        self.__members = []
        self.__leader = leader
        self.__tasks = []

    def getGroupName(self):
        return self.__groupName

    def getGroupID(self):
        return self.__groupId

    def getGroupLeader(self):
        return self.__leader

    def getMemberList(self):
        return self.__members

    def displayDetails(self):
        print(self.getGroupName())

    def addMember(self, new_member):
        self.__members.append(new_member)
