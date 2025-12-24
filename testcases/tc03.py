import ui_components
from classes import Student, Task


def tc03():
    print("\n\n\nTC-03: Adding Task")

    print("---Running Preconditions---")
    print("Creating new user...")
    new_user = Student("Tester", 123123, "test@gmail.com", "test", [])
    print("--- --- --- --- ---")

    print("Creating group...")
    group, message = new_user.createGroup("Test Group", 67)

    if group is not None:
        print(message)
        ui_components.displayDict("Created Group", group.getGroupInfo())
        print("Creating Task...")
        new_task = Task(
            1, "Test Case 3", "Testing for Case 3: Add Task", "29/12/2025", 5
        )
        if new_task is not None:
            group.addTasks(new_task)
            print(group.getTasks())
            print("Test case success! Task was added into Group.")
    else:
        print("Test case failed!, Failed to create Group")
