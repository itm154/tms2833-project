from classes import Group
import pickle
import os

DATA_DIR = "data"


def saveGroup(group: Group):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, f"group_{group.getGroupId()}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump(group, f)


def loadGroup(group_id: int) -> Group | None:
    file_path = os.path.join(DATA_DIR, f"group_{group_id}.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return None


def loadAllGroups() -> list[Group]:
    groups = []
    if os.path.exists(DATA_DIR):
        for filename in os.listdir(DATA_DIR):
            if filename.startswith("group_") and filename.endswith(".pkl"):
                group_id = int(filename.split("_")[1].split(".")[0])
                group = loadGroup(group_id)
                if group:
                    groups.append(group)
    return groups
