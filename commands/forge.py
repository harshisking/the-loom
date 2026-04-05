from core.session import get
from commands.utility import new, lst, archive
from core.paths import FORGE_DIR

forgedir = str(FORGE_DIR)


def forge():
    print("Forge")

    forge_help_msg = """Forge 
      help: This command allows you to forge new items.
      new: To forge a new item, use the command 'new <item-name>'.
      list: To list all existing forge projects. Use list <project-name> to list the contents in the project.
      archive: To archive a project in vault, use the command 'archive <project-name> [filetype]'. filetype is zip by default. 
      exit: To exit the forge, type 'exit'.
    """

    while True:
        forge_command = get("loom/forge>> ")

        if forge_command is None or forge_command.lower() == "exit":
            print("Forge Exiting")
            break

        elif forge_command.lower() == "help":
            print(forge_help_msg)

        elif forge_command.lower().startswith("new "):
            folname = forge_command.removeprefix("new ")
            new(folname, forgedir, "forge")

        elif forge_command.lower() == "list":
            lst(forgedir)

        elif forge_command.lower().startswith("list "):
            subpath = forge_command.removeprefix("list ")
            lst(f"{forgedir}/{subpath}")
        
        elif forge_command.lower().startswith("archive"):
            config = forge_command.removeprefix("archive ").split(" ")
            name = config[0]
            filetype = config[1] if len(config) > 1 else "zip"
            archive(name, filetype, forgedir)

        else:
            print("Unknown command. Type 'help' for a list of commands.")