from core.session import get


def smith():
    print("Smith")

    smith_help_msg = """Smith
        Help: Outputs this help message.
        exit: Exits the smith interface.
    """

    while True:
        smith_command = get("loom/smith>> ")

        if smith_command is None:
            break

        if smith_command.lower() == "exit":
            print("Smith Exiting")
            break

        elif smith_command.lower() == "help":
            print(smith_help_msg)

        else:
            print("Unknown command. Type 'help' for a list of commands.")