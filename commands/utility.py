import os
import shutil
from core.session import get, get_confirm


def new(s: str, path: str):
    if " " in s:
        s = s.replace(" ", "-")

    if "forge" in path:
        try:
            os.mkdir(f"{path}/{s}")
            open(f"{path}/{s}/README.md", "w").close()
            print(f"{s} folder created in forge with README.md.")
        except Exception as e:
            print(f"{e}")
    else:
        if not os.path.exists(f"{path}/{s}.md"):
            try:
                open(f"{path}/{s}.md", "w").close()
                print(f"{s}.md created in Blueprints.")
            except Exception as e:
                print(f"{e}")
        else:
            print(f"{s}.md already exists in Blueprints.")


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
        if os.path.exists(f"ideas/forge/{name}"):
            try:
                shutil.make_archive(f"ideas/vault/{name}", f"{filetype}", f"ideas/forge/{name}")
                print(f"{name} archived in vault successfully.")

                if get_confirm(f"Do you want to delete the original {name} from forge? (y/N): "):
                    shutil.rmtree(f"ideas/forge/{name}")
                else:
                    print(f"{name} retained in forge.")

            except Exception as e:
                print(f"ERROR: {e}")
        else:
            print(f"{name} does not exist in forge.")

def promote(name: str):
    if not os.path.exists(f"ideas/forge/{name}") and os.path.exists(f"ideas/blueprints/{name}.md"):
        os.makedirs(f"ideas/forge/{name}")
        shutil.move(f"ideas/blueprints/{name}.md", f"ideas/forge/README.md")
        print(f"{name} promoted from blueprints to forge.")
        