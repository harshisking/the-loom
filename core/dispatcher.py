import sys
from commands.forge import forge
from commands.blueprints import blueprints
from commands.vault import vault
from commands.smith import smith


def dispatch(command, help_msg):
    functions = {
        "exit": lambda: sys.exit("Exiting Loom"),
        "help": lambda: print(help_msg),
        "forge": forge,
        "blueprints": blueprints,
        "vault": vault,
        "smith": smith
    }

    if command in functions:
        functions[command]()
    else:
        print("Unknown command. Type 'help' for a list of commands.")