import os
import shutil
import logging
from core.session import get_confirm
from core.paths import LOG_FILE, VAULT_DIR, FORGE_DIR

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

def new(s: str, path: str, command: str):
    if " " in s:
        s = s.replace(" ", "-")

    if command == "forge":
        try:
            os.mkdir(f"{path}/{s}")
            logger.info(f"Created Folder: {path}/{s}")
            open(f"{path}/{s}/README.md", "w").close()
            logger.info(f"Created File: {path}/{s}/README.md")
            print(f"{s} folder created in forge with README.md.")
        except Exception as e:
            print(f"{e}")
            logger.exception(f"Fail Create: {path}/{s}/README.md")
    elif command == "blueprints":
        if not os.path.exists(f"{path}/{s}.md"):
            try:
                open(f"{path}/{s}.md", "w").close()
                logger.info(f"Created File: {path}/{s}.md")
                print(f"{s}.md created in Blueprints.")
            except Exception as e:
                print(f"{e}")
                logger.exception(f"Fail Create: {path}/{s}.md")
        else:
            print(f"{s}.md already exists in Blueprints.")
            logger.warning(f"Skip Create: {path}/{s}.md - Already Exists")


def lst(path: str):
    try:
        items = os.listdir(f"{path}")
        items = [item for item in items if not item.startswith(".")]

        if items:
            print(f"Items in {path}: ")
            for item in items:
                print(f"  - {item}")
            logger.info(f"List: {path}")
        else:
            print(f"No items found in {path}.")
            logger.info(f"List: {path} - Empty")
    except Exception as e:
        print(f"{e}")
        logger.exception(f"Fail List: {path}")


def archive(name: str, filetype: str, pathfrom: str):
        if os.path.exists(f"ideas/forge/{name}"):
            try:
                shutil.make_archive(f"{str(VAULT_DIR)}/{name}", f"{filetype}", f"{pathfrom}/{name}")
                logger.info(f"Archive Folder: {pathfrom}/{name} to {str(VAULT_DIR)}/{name}.{filetype}")
                print(f"{name} archived in vault successfully.")

                if get_confirm(f"Do you want to delete the original {name} from {pathfrom}? (y/N): "):
                    shutil.rmtree(f"{pathfrom}/{name}")
                    logger.info(f"Remove Folder: {pathfrom}/{name}")
                else:
                    print(f"{name} retained in forge.")
                    logger.info(f"Retain Folder: {pathfrom}/{name}")

            except Exception as e:
                print(f"ERROR: {e}")
                logger.exception(f"Fail Archive: {pathfrom}/{name}")
        else:
            print(f"{name} does not exist in forge.")
            logger.warning(f"Skip Archive: {pathfrom}/{name} - Not Exists")

def promote(name: str, pathfrom: str):
    if not os.path.exists(f"{str(FORGE_DIR)}/{name}"):
        if os.path.exists(f"{pathfrom}/{name}.md"):
            os.makedirs(f"{str(FORGE_DIR)}/{name}")
            logger.info(f"Created Folder: {str(FORGE_DIR)}/{name}")
            shutil.move(f"{pathfrom}/{name}.md", f"{str(FORGE_DIR)}/{name}/README.md")
            logger.info(f"Promote File: {pathfrom}/{name}.md to {str(FORGE_DIR)}/{name}/README.md")
            print(f"{name} promoted from blueprints to forge.")
        else:
            print(f"{name}.md doesn't exist in blueprints. Cannot promote.")
            logger.warning(f"Skip Promote: {pathfrom}/{name}.md - Not Exists")
    else:
        print(f"{name} already exists in forge. Cannot promote.")
        logger.warning(f"Skip Promote: {str(FORGE_DIR)}/{name} - Already Exists")
