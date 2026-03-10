import os

#######################
####### PATHS #########
#######################
forgepath = "ideas/forge"
blueprintspath = "ideas/blueprints"
vaultpath = "ideas/vault"

########################
#### MAIN FUNCTION #####
########################


def main():
    print("Loom Activated")

    loom_help_msg = """
    Available Commands:
        help : Display this help message
        exit : exit the loom
        forge : Forge an item
        vault : Access the vault
        smith : Visit the smith
        blueprints : Create a new blueprint
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
    Forge 
      Help: This command allows you to forge new items.
      New: To forge a new item, use the command 'new <item-name>'. This will create a new folder in the forge directory with the specified item name and a README.md file inside it.
      exit: To exit the forge, type 'exit'.
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

        elif forge_command.lower() == "list":
            lst(forgepath)
        
        elif forge_command.lower().startswith("list "):
            subpath = forge_command.removeprefix("list ")
            lst(f"{forgepath}/{subpath}")

        else:
            print("Unknown command. Type 'help' for a list of commands.")






def blueprints():
    print("Blueprint")
    blueprint_help_msg = """
    Blueprint 
      Help: This command allows you to create new blueprints.
      New: To create a new blueprint, use the command 'new <blueprint-name>'. This will create a new markdown file in the blueprints directory with the specified name.
      exit: To exit the blueprints interface, type 'exit'.
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
        
        elif blueprint_command.lower() == "list":
            lst(blueprintspath)

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
    if " " in s:
        s = s.replace(" ", "-")

    
    if command == "forge":
        try:
            os.makedirs(f"{forgepath}/{s}")
            open (f"{forgepath}/{s}/README.md", "w").close()
            print(f"{s} folder created in forge with README.md")
        except Exception as e:
            print(f"{e}")

    elif command == "blueprint":
        if not os.path.exists(f"{blueprintspath}/{s}.md"):
            open (f"{blueprintspath}/{s}.md", "w").close()
            print(f"{s}.md created in blueprints.")
        else:
            print(f"{s}.md already exists in blueprints.")

    
def lst(path:str):
    try:
        items = os.listdir(f"{path}")
        items = [item for item in items if not item.startswith(".")]  # Exclude hidden files
        if items:
            print(f"Items in {path}: ")
            for item in items:
                print(f"  - {item}")
        else:
            print(f"No items found in {path}.")
    except Exception as e:
        print(f"{e}")


##########################
####### FILE END #########
##########################

if __name__ == "__main__":    main()