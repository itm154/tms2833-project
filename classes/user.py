class User:
    def __init__(
        self, user_name: str, user_id: int, user_email: str, user_password: str
    ):
        self.__user_name = user_name
        self.__user_id = user_id
        self.__user_email = user_email
        self.__user_password = user_password

    def getUserName(self) -> str:
        return self.__user_name

    def getUserID(self) -> int:
        return self.__user_id

    def getUserEmail(self) -> str:
        return self.__user_email

    def getPassword(self) -> str:
        return self.__user_password


class Student(User):
    def __init__(
        self,
        user_name: str,
        matric_number: int,
        user_email: str,
        user_password: str,
        joined_groups: list,
    ):
        super().__init__(user_name, matric_number, user_email, user_password)
        self.__joined_groups = [] if joined_groups is None else joined_groups

    def getJoinedGroups(self) -> list:
        return self.__joined_groups

    def joinGroup(self, group_id: int):
        from data_manager import group_manager

        # Loads the group and adds the student in it
        temp_group = group_manager.loadGroup(group_id)

        if temp_group is None:
            return None, "Group not found."

        if self.getUserName() in temp_group.getMemberList():
            return (
                None,
                f"{self.getUserName()} is already a member of {temp_group.getGroupName()}.",
            )

        temp_group.addMember(self.getUserName())
        # Loads the student and updates student joined group list
        self.__joined_groups.append(group_id)
        return (
            temp_group,
            f"{self.getUserName()} successfully enrolled in group.",
        )

    def createGroup(self, group_name: str, group_id: int):
        from classes.group import Group

        new_group = Group(group_name, group_id, self.getUserName())
        return new_group, self.joinGroup(new_group.getGroupID())

    def viewGroup(self, group_id: int):
        from data_manager import group_manager

        temp_group = group_manager.loadGroup(group_id)
        if temp_group is None:
            return "No groups available."

        if self.getUserName() not in temp_group.getMemberList():
            return "You are not a member of this group."

        return {
            "group_name": temp_group.getGroupName(),
            "leader": temp_group.getGroupLeader(),
            "members": temp_group.getMemberList(),
            "tasks": temp_group.getTasks(),
        }


class Lecturer(User):
    def __init__(
        self, user_name, staff_id, user_email, user_password, office, faculty, course_id
    ):
        super().__init__(user_name, staff_id, user_email, user_password)
        self.__office = office
        self.__faculty = faculty
        self.__course_id = course_id

    def viewProgress():
        pass

    def generateReport():
        pass

    def giveComments():
        pass
