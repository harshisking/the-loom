from core.session import get


def vault():
    print("Vault")

    vault_help_msg = """
    Vault Help:
        This command allows you to access the vault.
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

        else:
            print("Unknown command. Type 'help' for a list of commands.")