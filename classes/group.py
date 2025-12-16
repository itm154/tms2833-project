from .user import Student


class Group:
    def __init__(
        self, groupName: str, groupId: int, members: list[Student], leader: Student
    ):
        self.__groupName = groupName
        self.__groupId = groupId
        self.__members = members
        self.__leader = leader
        self.__tasks = []
