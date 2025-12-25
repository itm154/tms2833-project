from random import randint


# Class: User
# Implemented by: Raimi Danial bin Mohd Radzi (102930)
class User:
    def __init__(
        self, user_name: str, user_id: int, user_email: str, user_password: str
    ):
        self._user_name = user_name
        self._user_id = user_id
        self._user_email = user_email
        self._user_password = user_password

    def getUserName(self) -> str:
        return self._user_name

    def getUserID(self) -> int:
        return self._user_id

    def getUserEmail(self) -> str:
        return self._user_email

    def getPassword(self) -> str:
        return self._user_password

    def getInfo(self) -> dict:
        return {
            "Username": self._user_name,
            "ID": self._user_id,
            "Email": self._user_email,
        }


# Class: Student
# Implemented by: Muhammad Ashrul Fahmi (102725)
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

    def getInfo(self) -> dict:
        info = super().getInfo()

        # Rename "ID" to matric number
        info["Matric Number"] = info.pop("ID")
        info["Joined Groups"] = self.getJoinedGroups()

        return info

    def joinGroup(self, group_id: int):
        from data_manager import group_manager, user_manager

        # Loads the group and adds the student in it
        temp_group = group_manager.loadGroup(group_id)

        if temp_group is None:
            return None, "Group not found."

        if self._user_name in temp_group.getMemberList():
            return (
                None,
                f"{self._user_name} is already a member of {temp_group.getGroupName()}.",
            )

        temp_group.addMember(self._user_name)
        group_manager.saveGroup(temp_group)

        # Loads the student and updates student joined group list
        self.__joined_groups.append(group_id)
        user_manager.saveUser(self)
        return (
            temp_group,
            f"{self._user_name} successfully enrolled in group.",
        )

    def createGroup(self, group_name: str, group_id: int):
        from classes.group import Group
        from data_manager import group_manager

        new_group = Group(group_name, group_id, self._user_name)
        group_manager.saveGroup(new_group)
        joined_group, message = self.joinGroup(group_id)
        return joined_group, f"Group created. {message}"

    def viewGroup(self, group_id: int):
        from data_manager import group_manager

        temp_group = group_manager.loadGroup(group_id)
        if temp_group is None:
            return "No groups available."

        if self._user_name not in temp_group.getMemberList():
            return "You are not a member of this group."

        return {
            "group_name": temp_group.getGroupName(),
            "leader": temp_group.getGroupLeader(),
            "members": temp_group.getMemberList(),
            "tasks": temp_group.getTasks(),
        }


# Class: Lecturer
# Implemented by: Seng Zhi Jie (106256)
class Lecturer(User):
    def __init__(
        self, user_name, staff_id, user_email, user_password, office, faculty, course_id
    ):
        super().__init__(user_name, staff_id, user_email, user_password)
        self.__office = office
        self.__faculty = faculty
        self.__course_id = course_id

    def getInfo(self) -> dict:
        info = super().getInfo()

        # Rename "ID" to "Staff ID"
        info["Staff ID"] = info.pop("ID")
        info["Faculty"] = self.__faculty
        info["Office"] = self.__office
        info["Course"] = self.__course_id

        return info

    def viewGroup(self, group_id: int):
        from data_manager import group_manager

        temp_group = group_manager.loadGroup(group_id)
        if temp_group is None:
            return "No groups available."

        return {
            "group_name": temp_group.getGroupName(),
            "leader": temp_group.getGroupLeader(),
            "members": temp_group.getMemberList(),
            "tasks": temp_group.getTasks(),
        }

    def generateReport(self, group_id: int):
        from classes.report import Report
        from data_manager import group_manager

        temp_group = group_manager.loadGroup(group_id)
        if temp_group is None:
            return "No groups available."

        report = Report(randint(100000, 999999), temp_group).getReport()
        return report

    def giveComments(self, group_id: int, task: str, comment: str):
        return f"Lecturer {self._user_name} comments on task {task} : {comment}"
