class User:
    def _init_(self, userName: str, userID: int, userEmail: str, password: str):
        self.__userName = userName
        self.__userID = userID
        self.__userEmail = userEmail
        self.__password = password


class Student(User):
    def joinGroup(self):
        pass

    def createGroup(self):
        pass

    def viewDashboard(self):
        pass

    def viewTask(self):
        pass


class Lecturer(User):
    def __init__(self, office, faculty, courseID):
        super().__init__()
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
