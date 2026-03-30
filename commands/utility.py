import os
import shutil
import logging
from core.session import get_confirm

logging.basicConfig(
    filename="loom.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

def new(s: str, path: str):
    if " " in s:
        s = s.replace(" ", "-")

    if "forge" in path:
        try:
            os.mkdir(f"{path}/{s}")
            logger.info(f"Created Folder: {path}/{s}")
            open(f"{path}/{s}/README.md", "w").close()
            logger.info(f"Created File: {path}/{s}/README.md")
            print(f"{s} folder created in forge with README.md.")
        except Exception as e:
            print(f"{e}")
            logger.exception(f"Fail Create: {path}/{s}/README.md")
    else:
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


def archive(name: str, filetype: str):
        if os.path.exists(f"ideas/forge/{name}"):
            try:
                shutil.make_archive(f"ideas/vault/{name}", f"{filetype}", f"ideas/forge/{name}")
                logger.info(f"Archive Folder: ideas/forge/{name} to ideas/vault/{name}.{filetype}")
                print(f"{name} archived in vault successfully.")

                if get_confirm(f"Do you want to delete the original {name} from forge? (y/N): "):
                    shutil.rmtree(f"ideas/forge/{name}")
                    logger.info(f"Remove Folder: ideas/forge/{name}")
                else:
                    print(f"{name} retained in forge.")
                    logger.info(f"Retain Folder: ideas/forge/{name}")

            except Exception as e:
                print(f"ERROR: {e}")
                logger.exception(f"Fail Archive: ideas/forge/{name}")
        else:
            print(f"{name} does not exist in forge.")
            logger.warning(f"Skip Archive: ideas/forge/{name} - Not Exists")

def promote(name: str):
    if not os.path.exists(f"ideas/forge/{name}"):
        if os.path.exists(f"ideas/blueprints/{name}.md"):
            os.makedirs(f"ideas/forge/{name}")
            logger.info(f"Created Folder: ideas/forge/{name}")
            shutil.move(f"ideas/blueprints/{name}.md", f"ideas/forge/{name}/README.md")
            logger.info(f"Promote File: ideas/blueprints/{name}.md to ideas/forge/{name}/README.md")
            print(f"{name} promoted from blueprints to forge.")
        else:
            print(f"{name}.md doesn't exist in blueprints. Cannot promote.")
            logger.warning(f"Skip Promote: ideas/blueprints/{name}.md - Not Exists")
    else:
        print(f"{name} already exists in forge. Cannot promote.")
        logger.warning(f"Skip Promote: ideas/forge/{name} - Already Exists")
