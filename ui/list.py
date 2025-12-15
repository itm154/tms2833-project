def display_list(title: str, items: list):
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


def display_numbered_list(title: str, items: list):
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
