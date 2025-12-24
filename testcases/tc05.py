from datetime import datetime

import ui_components
from classes import Student, Task


def tc05():
    print("\n\n\nTC-05: Update task")

    print("--- Running Preconditions ---")
    print("Creating new user...")
    new_user = Student("Tester", 123123, "test@gmail.com", "test", [])

    print("Creating group...")
    group, message = new_user.createGroup("Test Group", 123)

    print("Adding sample task to group...")
    sample_task = Task(
        1,
        "Test task",
        "Just a test",
        datetime.now().date(),
        5,
        "To Do",
    )

    if group is not None:
        group.addTasks(sample_task)

        print("--- --- --- --- ---")
        print("Updating task...")

        task = group.getTaskById(1)
        if task is not None:
            task.editTask(
                "New title",
                "Edited Description",
                datetime.strptime("30/12/2025", "%d/%m/%Y").date(),
                3,
            )
            ui_components.displayDict("Task information", task.getInfo())
            print("Test case 5 passed!")
        else:
            print("Test case failed!")
            print("Failed to update task!")
