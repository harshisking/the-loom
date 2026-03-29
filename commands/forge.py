from core.session import get
from commands.utility import new, lst, archive

forgepath = "ideas/forge"


def forge():
    print("Forge")

    forge_help_msg = """Forge 
      Help: This command allows you to forge new items.
      New: To forge a new item, use the command 'new <item-name>'.
      exit: To exit the forge, type 'exit'.
    """

    while True:
        forge_command = get("loom/forge>> ")

        if forge_command is None:
            break
       
        elif forge_command.lower() == "exit":
            print("Forge Exiting")
            break

        elif forge_command.lower() == "help":
            print(forge_help_msg)

        elif forge_command.lower().startswith("new "):
            folname = forge_command.removeprefix("new ")
            new(folname, forgepath)

        elif forge_command.lower() == "list":
            lst(forgepath)

        elif forge_command.lower().startswith("list "):
            subpath = forge_command.removeprefix("list ")
            lst(f"{forgepath}/{subpath}")
        
        elif forge_command.lower().startswith("archive"):
            config = forge_command.removeprefix("archive ").split(" ")
            name = config[0]
            filetype = config[1] if len(config) > 1 else "zip"
            archive(name,filetype)

        else:
            print("Unknown command. Type 'help' for a list of commands.")