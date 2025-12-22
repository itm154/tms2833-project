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

    def getInfo(self) -> dict:
        return {
            "Username": self.__user_name,
            "ID": self.__user_id,
            "Email": self.__user_email,
        }


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

        if self.getUserName() in temp_group.getMemberList():
            return (
                None,
                f"{self.getUserName()} is already a member of {temp_group.getGroupName()}.",
            )

        temp_group.addMember(self.getUserName())
        group_manager.saveGroup(temp_group)

        # Loads the student and updates student joined group list
        self.__joined_groups.append(group_id)
        user_manager.saveUser(self)
        return (
            temp_group,
            f"{self.getUserName()} successfully enrolled in group.",
        )

    def createGroup(self, group_name: str, group_id: int):
        from classes.group import Group
        from data_manager import group_manager

        new_group = Group(group_name, group_id, self.getUserName())
        group_manager.saveGroup(new_group)
        joined_group, message = self.joinGroup(group_id)
        return joined_group, f"Group created. {message}"

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

    def viewProgress(self, group_id: int):
        from data_manager import group_manager
        
        temp_group = group_manager.loadGroup(group_id)
        if temp_group is None:
            return "No groups available."

        task = temp_group.getTask()
        if task is None:
            return "Task is not assigned to this group."

        total_tasks = len(tasks)
        completed = sum(1 for task in tasks if task.get("status") == "Completed")
        percentage = (completed/total_tasks) * 100

        return f"Group {group_id} Progress: {percentage:.2f}% done"
                 
    def generateReport(self, group_id: int, report_id: int):
        from data_manager import group_manager
        from datetime import datetime 
        
        temp_group = group_manager.loadGroup(group_id)
        if temp_group is None:
            return "No groups available.Report cannot be Generated!"

        task = temp_group.getTask()
        if task is None:
            return "No task is found to generate report."
            
        total_tasks = len(tasks)
        completed = sum(1 for task in task if task.get('status') == 'Completed')

        report = {
           "report_id" = report_id,
           "generated_date" = datetime.now(),
           "total_tasks" = total_tasks,
           "completed_tasks" = completed_tasks,
           "Report Summary"= "Sum generated by Lecturer"
        }
        return new_Report

    def giveComments(self, group_id: int, task: str, comment:str):
        return f"Lecturer {self.getUserName()} comments on task {task} : {comment}"
