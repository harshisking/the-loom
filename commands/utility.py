import os

forgepath = "ideas/forge"
blueprintspath = "ideas/blueprints"
vaultpath = "ideas/vault"


def new(s: str, command: str):
    if " " in s:
        s = s.replace(" ", "-")

    if command == "forge":
        try:
            os.makedirs(f"{forgepath}/{s}")
            open(f"{forgepath}/{s}/README.md", "w").close()
            print(f"{s} folder created in forge with README.md")
        except Exception as e:
            print(f"{e}")

    elif command == "blueprint":
        if not os.path.exists(f"{blueprintspath}/{s}.md"):
            open(f"{blueprintspath}/{s}.md", "w").close()
            print(f"{s}.md created in blueprints.")
        else:
            print(f"{s}.md already exists in blueprints.")


def lst(path: str):
    try:
        items = os.listdir(f"{path}")
        items = [item for item in items if not item.startswith(".")]

        if items:
            print(f"Items in {path}: ")
            for item in items:
                print(f"  - {item}")
        else:
            print(f"No items found in {path}.")
    except Exception as e:
        print(f"{e}")