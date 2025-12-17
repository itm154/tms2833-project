class User:
    def __init__(self, userName: str, userID: int, userEmail: str, userPassword: str):
        self.__userName = userName
        self.__userID = userID
        self.__userEmail = userEmail
        self.__password = userPassword

    def getUserName(self) -> str:
        return self.__userName

    def getUserID(self) -> int:
        return self.__userID

    def getUserEmail(self) -> str:
        return self.__userEmail

    def setUserEmail(self, userEmail: str):
        self.__userEmail = userEmail

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, userPassword: str):
        self.__password = userPassword


class Student(User):
    def __init__(
        self,
        userName: str,
        matricNumber: int,
        userEmail: str,
        userPassword: str,
        joinedGroups: list,
    ):
        super().__init__(userName, matricNumber, userEmail, userPassword)
        self.__joinedGroups = [] if joinedGroups is None else joinedGroups

    def getJoinedGroups(self) -> list:
        return self.__joinedGroups

    def joinGroup(self, group):
        self.__joinedGroups.append(group)
        return


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
