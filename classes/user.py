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

    def getPassword(self) -> str:
        return self.__password


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

    def joinGroup(self, groupID: int):
        import groupManager
        import auth

        # Loads the group and adds the student in it
        temp_group = groupManager.load_group(groupID)

        if temp_group is None:
            print("Group not found.")
            return

        if self.getUserName() in temp_group.getMemberList():
            print(
                f"{self.getUserName()} is already a member of {temp_group.getGroupName()}."
            )
            return

        temp_group.addMember(self.getUserName())
        groupManager.save_group(temp_group)
        # Loads the student and updates student joined group list
        self.__joinedGroups.append(groupID)
        auth.save_user(self)
        print(f"{self.getUserName()} successfully enrolled in group.")

    def createGroup(self):
        import ui
        from classes.group import Group
        import groupManager

        # Prompt Group Details
        name = str(input("Please enter Group Name: "))
        id = ui.numeric_input("Please enter Group ID: ")

        newGroup = Group(name, id, self.getUserName())
        groupManager.save_group(newGroup)
        print("Group created successfully.")
        self.joinGroup(newGroup.getGroupID())

    def viewGroup(self, groupID: int):
        import groupManager
        import ui

        temp_group = groupManager.load_group(groupID)
        if temp_group is None:
            print("No groups available.")
            return

        if self.getUserName() not in temp_group.getMemberList():
            print("You are not a member of this group.")
            return

        print(f"Group Name: {temp_group.getGroupName()}")
        print(f"Leader: {temp_group.getGroupLeader()}")
        ui.display_list("Members", temp_group.getMemberList())
        print("Tasks: ")


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
