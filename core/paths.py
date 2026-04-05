from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
IDEAS_DIR = Path(os.getenv("LOOM_IDEAS_DIR", ROOT / "ideas"))
FORGE_DIR = Path(os.getenv("LOOM_FORGE_DIR", IDEAS_DIR / "forge"))
BLUEPRINTS_DIR = Path(os.getenv("LOOM_BLUEPRINTS_DIR", IDEAS_DIR / "blueprints"))
VAULT_DIR = Path(os.getenv("LOOM_VAULT_DIR", IDEAS_DIR / "vault"))
LOG_FILE = Path(os.getenv("LOOM_LOG_FILE", ROOT / "loom.log"))

# Ensure configured storage locations exist even when overridden via env vars.
for directory in (IDEAS_DIR, FORGE_DIR, BLUEPRINTS_DIR, VAULT_DIR):
	directory.mkdir(parents=True, exist_ok=True)

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
