# Usage
# choice = ui.select("Select one", ["thing 1", "Thing 2", "Thing 3"])
#
# match choice:
#     case 1:
#         print("doing thing 1")
# ...


def select(title: str, options: list[str]) -> int:
    titlebar = f"--- {title} ---"
    print(titlebar)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    while True:
        try:
            choice = input(f"[1-{len(options)}] > ")
            if 0 <= int(choice) - 1 < len(options):
                return int(choice)
            else:
                print("Error: Invalid choice. Please try again.")
        except ValueError:
            print("Error: Invalid Input. Please enter a number.")
