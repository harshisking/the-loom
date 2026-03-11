# Loom

**Loom** is a terminal-first idea development system designed to help structure and manage thoughts, concepts, and projects directly from the command line.

The system organizes ideas into three primary stages:

- **Blueprints** → Raw sparks and early ideas  
- **Forge** → Active ideas currently being developed  
- **Vault** → Archived or completed ideas  

Workflow philosophy:

Blueprint → Forge → Vault


---

# Project Structure

loom/
│
├── commands/            # Command interfaces
│   ├── forge.py
│   ├── blueprints.py
│   ├── vault.py
│   ├── smith.py
│   └── utility.py
│
├── core/                # Core system components
│   ├── session.py
│   └── dispatcher.py
│
├── ideas/               # Idea storage
│   ├── forge/
│   ├── blueprints/
│   └── vault/
│
└── loom.py              # Application entry point


---

# Requirements

- Python 3.8+
- prompt_toolkit


---

# Installation

Clone the repository:

git clone <repository-url>
cd loom

Install dependencies:

pip install -r requirements.txt


---

# Running Loom

Start the application:

python loom.py

Expected output:

Loom Activated
loom>>


---

# Commands

help        Show available commands  
forge       Open the Forge interface  
blueprints  Open the Blueprints interface  
vault       Open the Vault interface  
smith       Open the Smith interface  
exit        Exit Loom  


---

# Forge

The **Forge** is used for active development of ideas.

Commands inside Forge:

help            Show Forge help  
new <name>      Create a new idea folder  
list            List Forge items  
list <path>     List items inside a Forge subfolder  
exit            Exit Forge  

Creating a new item generates:

ideas/forge/<item-name>/
└── README.md


---

# Blueprints

The **Blueprints** area stores raw concepts.

Commands inside Blueprints:

help            Show Blueprints help  
new <name>      Create a new blueprint file  
list            List blueprint files  
exit            Exit Blueprints  

Blueprint files are stored as:

ideas/blueprints/<name>.md


---

# Vault

The **Vault** stores archived or completed ideas.

Commands inside Vault:

help        Show Vault help  
exit        Exit Vault  


---

# Smith

The **Smith** interface is reserved for future functionality.

Commands inside Smith:

help        Show Smith help  
exit        Exit Smith  


---

# Philosophy

Loom is designed around the concept that ideas evolve through stages:

1. Blueprint – the initial spark  
2. Forge – active development and refinement  
3. Vault – archived or completed work  

The terminal-first design keeps the system minimal and focused on thinking and idea development.


---

# License

license specified.