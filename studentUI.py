import groupManager
import ui


def studentMenu(authenticatedUser):
    while True:
        choice = ui.select(
            "Please Select An Action",
            ["Create Group", "Join Group", "View Group", "Log Out"],
        )
        match choice:
            case 1:
                groupManager.createGroup(authenticatedUser)
                # Student Creates a Group
            case 2:
                pass
                # Student Joins a Group
            case 3:
                groupManager.viewGroup(authenticatedUser)
                # This function was used to test group adding only, can change the logic of the function to it's intended use.
                # Student Views an Existing Group
            case 4:
                # Logging out
                break
