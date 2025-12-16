class Group:
    def __init__(self, groupName: str, groupId: int, members: list, leader):
        self.__groupName = groupName
        self.__groupId = groupId
        # Members should be only the leader after creation for now
        self.__members = [leader]
        self.__leader = leader
        self.__tasks = []
