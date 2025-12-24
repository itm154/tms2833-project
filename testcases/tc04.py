import ui_components
from classes import Student


# Test Case 4
# Implemented by: Seng Zhi Jie (106256)
def tc04():
    print("\n\n\nTC-04: Join Group")

    print("Creating group user...")
    owner = Student("Tester", 121213, "test@gmail.com", "Test", [])
    print("Creating joining student...")
    joiner = Student("Tester 4", 121214, "test4@gmail.com", "Test4", [])

    print("Creating test group....")
    group, create_message = owner.createGroup("Test 4 Group", 4)
    print(create_message)

    if group is None:
        print("Test case failed! Group creation failed.")
        return
    ui_components.displayDict("Group successfully created", group.getGroupInfo())

    print("Joining group...")
    joined_group, join_message = joiner.joinGroup(group.getGroupId())
    print(join_message)

    if joined_group is None:
        print("Test case failed! Student failed to join group.")
        return

    print("Test case passed! Student joined the group successfully.")
