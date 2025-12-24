from classes import Lecturer


def tc02():
    print("TC-02: Failed to generate report")

    print("Creating new user...")
    new_user = Lecturer(
        "Lecturer1",
        123123,
        "lecturer@staff.com",
        "password",
        "CUBE",
        "FCSIT",
        "TMS2388",
    )

    print("Trying to generate report on a group that doesn't exist...")
    report = new_user.generateReport(987654)  # Random group id that doesnt exist

    if isinstance(report, dict):
        print("Test case failed! Group report created on a group that does not exist!")
    else:
        print("Test case pass!")
        print("Message: " + report)
