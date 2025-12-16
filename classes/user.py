class User:
    def __init__(self, userName: str, userID: int, userEmail: str, password: str):
        self.__userName = userName
        self.__userID = userID
        self.__userEmail = userEmail
        self.__password = password

    def getUserName(self) -> str:
        return self.__userName

    def setUserName(self, userName: str):
        self.__userName = userName

    def getUserID(self) -> int:
        return self.__userID

    def setUserID(self, userID: int):
        self.__userID = userID

    def getUserEmail(self) -> str:
        return self.__userEmail

    def setUserEmail(self, userEmail: str):
        self.__userEmail = userEmail

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, password: str):
        self.__password = password


class Student(User):
    def __init__(
        self,
        userName: str,
        matricNumber: int,
        userEmail: str,
        password: str,
        joinedGroups: list[int],
    ):
        super().__init__(userName, matricNumber, userEmail, password)
        self.__joinedGroups = [] if joinedGroups is None else joinedGroups

    def getJoinedGroups(self) -> list:
        return self.__joinedGroups

    def joinGroup(self, groupID: int):
        self.__joinedGroups.append(groupID)


class Lecturer(User):
    def __init__(
        self, userName, userID, userEmail, password, office, faculty, courseID
    ):
        super().__init__(userName, userID, userEmail, password)
        self.__office = office
        self.__faculty = faculty
        self.__courseID = courseID

    def viewProgress():
        pass

    def generateReport():
        pass

    def giveComments():
        pass

    def viewTask():
        pass
