import data_manager
import ui_components
from classes import Group, Task


def groupMenu(group: Group):
    while True:
        choice = ui_components.select(
            "Task Menu",
            [
                "Add Task",
                "View Tasks",
                "Edit Task",
                "Delete Task",
                "Assign Task",
                "Update Task Status",
                "View group information",
                "Back",
            ],
        )

        match choice:
            case 1:
                # Add Task
                task_id = ui_components.numericInput("Task ID: ")
                title = input("Title: ")
                description = input("Description: ")
                deadline = input("Deadline: ")
                priority = ui_components.numericInput("Priority (1-5): ")
                task = Task(task_id, title, description, deadline, priority)

                group.addTasks(task)
                data_manager.saveGroup(group)
                print(f"Task '{title}' created.")

                # View Task
            case 2:
                tasks = group.getTasks()

                if not tasks:
                    print("No tasks in this group yet.")
                else:
                    for t in tasks:
                        t.displayTaskInfo()

                # Edit Task
            case 3:
                task_id = ui_components.numericInput("Enter Task ID to edit: ")
                task = group.getTaskById(task_id)

                if task is None:
                    print("Task not found.")
                else:
                    print("\nEditing Task:")
                    task.displayTaskInfo()
                    new_title = input("New Title: ")
                    new_desc = input("New Description: ")
                    new_deadline = input("New Deadline: ")
                    new_priority = ui_components.numericInput("New Priority (1-5): ")
                    task.editTask(new_title, new_desc, new_deadline, new_priority)

                    data_manager.saveGroup(group)
                    print("Task updated successfully.")

                # Delete Task
            case 4:
                task_id = ui_components.numericInput("Enter Task ID to delete: ")

                success = group.deleteTaskById(task_id)

                if success:
                    data_manager.saveGroup(group)
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")

                # AssignTo
            case 5:
                task_id = ui_components.numericInput("Enter Task ID: ")
                task = group.getTaskById(task_id)

                if task is None:
                    print("Task not found.")
                else:
                    username = input("Enter username to assign: ")
                    task.assignTo(username)
                    data_manager.saveGroup(group)

                # UpdateStatus
            case 6:
                task_id = ui_components.numericInput("Enter Task ID: ")
                task = group.getTaskById(task_id)

                if task is None:
                    print("Task not found.")
                else:
                    new_status = input(
                        "Enter new status (To Do / In Progress / Done): "
                    )
                    task.updateStatus(new_status)
                    data_manager.saveGroup(group)

            case 7:
                ui_components.displayDict("Group information", group.getGroupInfo())

            case 8:
                break
