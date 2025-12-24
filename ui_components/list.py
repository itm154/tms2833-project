# Usage
# somelist = ["person 1", "person2", "person3"]
# ui.display_list("Title", somelist)

# User Interface Components for Selecting Group
# Implemented by: Seng Zhi Jie (106256)
def displayList(title: str, items: list):
    titlebar = f"\n--- {title} ---"
    closing_line = "-" * len(titlebar)
    print(titlebar)

    if not items:
        print("No entries")
        return

    for i, item in enumerate(items):
        print(f"{item}")
    print(closing_line)
    print()


def displayNumberedList(title: str, items: list):
    titlebar = f"\n--- {title} ---"
    closing_line = "-" * len(titlebar)
    print(titlebar)

    if not items:
        print("No entries")
        return

    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")
    print(closing_line)
    print()


def displayDict(title: str, data: dict):
    titlebar = f"\n--- {title} ---"
    closing_line = "-" * len(titlebar)
    print(titlebar)

    if not data:
        print("No entries")
        return

    for key, value in data.items():
        print(f"{key}: {value}")
    print(closing_line)
    print()
