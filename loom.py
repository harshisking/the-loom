from core.session import get
from core.dispatcher import dispatch


def main():
    print("Loom Activated")

    loom_help_msg = """Available Commands:
        help : Display this help message
        exit : exit the loom
        forge : Access the forge
        vault : Access the vault
        smith : Visit the smith
        blueprints : Access the blueprints
        """

    while True:
        command = get("loom> ")
        if command is None:
            print("Exiting Loom...")
            break

        dispatch(command, loom_help_msg)


if __name__ == "__main__":
    main()