import pickle
import os
from classes import User

DATA_DIR = "data"


def save_user(user: User):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file_path = os.path.join(DATA_DIR, f"{user.getUserName()}.pkl")
    with open(file_path, "wb") as f:
        pickle.dump(user, f)


def load_user(username: str) -> User | None:
    file_path = os.path.join(DATA_DIR, f"{username}.pkl")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    return None
