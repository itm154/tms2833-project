import data_manager
import ui_components
from classes import Group, Task


def taskMenu(group: Group):
    while True:
        choice = ui_components.select(
            "Task Menu",
            ["Add Task", "View Tasks", "Edit Task", "Delete Task", "Back"],
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
                task.createTask()
                group.addTasks(task)
                data_manager.saveGroup(group)

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

            case 5:
                break
