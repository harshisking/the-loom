import os

def main():
    print("Loom Activated")

    loom_help_msg = """
    Available Commands:
        help : Display this help message
        exit : exit the loom
        forge : Forge an item
        vault : Access the vault
        smith : Visit the smith
        """
    
    while True:
        command = input("loom>> ").lower()
    
        if command == "exit":
            print("Loom Exiting")
            break
    
        elif command == "help":
            print(loom_help_msg)
        
        elif command == "forge":
            forge()
        
        elif command == "blueprints":
            blueprints()

        elif command == "vault":
            vault()

        elif command == "smith":
            smith()
        
        else:
            print("Unknown command. Type 'help' for a list of commands.")


######################
### CORE FUNCTIONS ###
######################

def forge():
    print("Forge")
    forge_help_msg = """
    Forge Help:
        This command allows you to forge new items.
    """
    while True:
        forge_command = input("loom/forge>> ").strip()

        if forge_command.lower() == "exit":
            print("Forge Exiting")
            break

        elif forge_command.lower() == "help":
            print(forge_help_msg)

        elif forge_command.lower().startswith("new "):
            folname = forge_command.removeprefix("new ")
            new(folname, "forge")

        else:
            print("Unknown command. Type 'help' for a list of commands.")


def blueprints():
    print("Blueprint")
    blueprint_help_msg = """
    Blueprint Help:
        This command allows you to create new blueprints.
    """

    while True:
        blueprint_command = input("loom/blueprint>> ").strip()

        if blueprint_command.lower() == "exit":
            print("Blueprint Exiting")
            break

        elif blueprint_command.lower() == "help":
            print(blueprint_help_msg)

        elif blueprint_command.lower().startswith("new "):
            fname = blueprint_command.removeprefix("new ")
            new(fname, "blueprint")

        else:
            print("Unknown command. Type 'help' for a list of commands.")

def vault():
    print("Vault")
    vault_help_msg = """
    Vault Help:
        This command allows you to access the vault.
    """

    while True:
        vault_command = input("loom/vault>> ").strip()

        if vault_command.lower() == "exit":
            print("Vault Exiting")
            break

        elif vault_command.lower() == "help":
            print(vault_help_msg)

        else:
            print("Unknown command. Type 'help' for a list of commands.")


def smith():
    print("Smith")
    smith_help_msg = """
    Smith Help:
        This command allows you to visit the smith.
    """

    while True:
        smith_command = input("loom/smith>> ").strip()

        if smith_command.lower() == "exit":
            print("Smith Exiting")
            break

        elif smith_command.lower() == "help":
            print(smith_help_msg)

        else:
            print("Unknown command. Type 'help' for a list of commands.")

#####################
# UTILITY FUNCTIONS #
#####################

def new(s:str, command:str):
    # eliminating spaces and replacing with "-"
    try:
        s =  s.replace(" ", "-")
    except Exception as e:
        pass

    
    if command == "forge":
        try:
            os.makedirs(f"ideas/forge/{s}")
            open (f"ideas/forge/{s}/README.md", "w").close()
            print(f"{s} folder created in forge with README.md")
        except Exception as e:
            print(f"{e}")

    elif command == "blueprint":
        if not os.path.exists(f"ideas/blueprints/{s}.md"):
            open (f"ideas/blueprints/{s}.md", "w").close()
            print(f"{s}.md created in blueprints.")
        else:
            print(f"{s}.md already exists in blueprints.")

    



##########################
####### FILE END #########
##########################

if __name__ == "__main__":    main()