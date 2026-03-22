from core.session import get
from commands.utility import lst

vaultpath = "ideas/vault"


def vault():
    print("Vault")

    vault_help_msg = """Vault
        Help: This command allows you to access the vault.
        exit: Exits the vault interface.
    """

    while True:
        vault_command = get("loom/vault>> ")
        
        if vault_command is None:
            break

        if vault_command.lower() == "exit":
            print("Vault Exiting")
            break

        elif vault_command.lower() == "help":
            print(vault_help_msg)

        elif vault_command.lower() == "list":
            lst(vaultpath)
        
        elif vault_command.lower().startswith("list "):
            subpath = vault_command.removeprefix("list ")
            lst(f"{vaultpath}/{subpath}")
            
        else:
            print("Unknown command. Type 'help' for a list of commands.")