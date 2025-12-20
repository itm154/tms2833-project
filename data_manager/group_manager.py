from classes import Group
import pickle
import os

DATA_DIR = "data"


def saveGroup(group: Group):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, f"group_{group.getGroupID()}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump(group, f)


def loadGroup(group_id: int) -> Group | None:
    file_path = os.path.join(DATA_DIR, f"group_{group_id}.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return None
