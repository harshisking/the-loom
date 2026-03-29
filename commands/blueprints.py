from core.session import get, ses
from commands.utility import new, lst

blueprintspath = "ideas/blueprints"


def blueprints():
    print("Blueprints")

    blueprint_help_msg = """Blueprints 
      Help: This command allows you to create new blueprints.
      New: To create a new blueprint, use the command 'new <blueprint-name>'.
      exit: To exit the blueprints interface, type 'exit'.
    """

    while True:
        blueprint_command = get("loom/blueprints>> ")

        if blueprint_command is None:
            break
        
        if blueprint_command.lower() == "exit":
            print("Blueprints Exiting")
            break

        elif blueprint_command.lower() == "help":
            print(blueprint_help_msg)

        elif blueprint_command.lower().startswith("new "):
            fname = blueprint_command.removeprefix("new ")
            new(fname, blueprintspath)

        elif blueprint_command.lower() == "list":
            lst(blueprintspath)

        else:
            print("Unknown command. Type 'help' for a list of commands.")