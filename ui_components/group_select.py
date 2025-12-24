from data_manager import group_manager
from .select import select
from classes import Group
from typing import List


# Parameter for group can either be a list (of joined groups for students) or nothing (for lecturer cus they can see all)
def selectGroup(
    title: str = "Select Group", groups_list: List[Group] | None = None
) -> Group | None:
    groups = groups_list if groups_list is not None else group_manager.loadAllGroups()

    if not groups:
        print("No groups found.")
        return None

    group_names = [group.getGroupName() for group in groups]
    choice_index = select(title, group_names)

    # select returns 1-based index, so convert to 0-based
    selected_group = groups[choice_index - 1]
    return selected_group


def selectGroupID(
    title: str = "Select Group", groups_list: List[Group] | None = None
) -> int | None:
    selected_group = selectGroup(title, groups_list)
    if selected_group:
        return selected_group.getGroupId()
    return None
