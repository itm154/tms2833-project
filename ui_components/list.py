# Usage
# somelist = ["person 1", "person2", "person3"]
# ui.display_list("Title", somelist)


def displayList(title: str, items: list):
    titlebar = f"--- {title} ---"
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
    titlebar = f"--- {title} ---"
    closing_line = "-" * len(titlebar)
    print(titlebar)

    if not items:
        print("No entries")
        return

    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")
    print(closing_line)
    print()
