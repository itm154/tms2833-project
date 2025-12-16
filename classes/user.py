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
    pass
