class User:
    def _init_(self, userName, userID, userEmail, password, groupID):
        self.userName = userName
        self.userID = userID
        self.userEmail = userEmail
        self.password = password
        self.groupID = groupID
        self.Loggedin = false

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
