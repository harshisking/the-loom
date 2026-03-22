import os
import shutil

from core.session import get, get_confirm

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


def archive(name: str, filetype: str):
        if os.path.exists(f"{forgepath}/{name}"):
            try:
                shutil.make_archive(f"{vaultpath}/{name}", f"{filetype}", f"{forgepath}/{name}")
                print(f"{name} archived in vault successfully.")

                if get_confirm(f"Do you want to delete the original {name} from forge? (y/N): "):
                    shutil.rmtree(f"{forgepath}/{name}")
                else:
                    print(f"{name} retained in forge.")

            except Exception as e:
                print(f"ERROR: {e}")
        else:
            print(f"{name} does not exist in forge.")

def promote(name: str):
    if not os.path.exists(f"{forgepath}/{name}"):
        os.makedirs(f"{forgepath}/{name}")
        shutil.move(f"{blueprintspath}/{name}.md", f"{forgepath}/README.md")
        print(f"{name} promoted from blueprints to forge.")
        