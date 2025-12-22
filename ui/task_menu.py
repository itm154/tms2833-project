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

                group.addTasks(task)
                data_manager.saveGroup(group)
                print("Task created successfully.")

            case 2:
                break
