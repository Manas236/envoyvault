import os
import json
from pathlib import Path

class VaultManager:
    def __init__(self, storage_path="~/.envoyvault/vault.json"):
        self.vault_path = Path(storage_path).expanduser()
        self.vault_dir = self.vault_path.parent
        self._ensure_vault_exists()

    def _ensure_vault_exists(self):
        if not self.vault_dir.exists():
            self.vault_dir.mkdir(parents=True, mode=0o700)
        if not self.vault_path.exists():
            with open(self.vault_path, 'w') as f:
                json.dump({"active": None, "projects": {}}, f)
            os.chmod(self.vault_path, 0o600)

    def _load_data(self):
        with open(self.vault_path, 'r') as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.vault_path, 'w') as f:
            json.dump(data, f, indent=4)

    def add_project(self, name, variables):
        data = self._load_data()
        data["projects"][name] = variables
        self._save_data(data)

    def list_projects(self):
        data = self._load_data()
        return list(data["projects"].keys())

    def switch_project(self, name):
        data = self._load_data()
        if name in data["projects"]:
            data["active"] = name
            self._save_data(data)
            return True
        return False

    def get_active_vars(self):
        data = self._load_data()
        active = data.get("active")
        if active and active in data["projects"]:
            return data["projects"][active]
        return None

    def export_shell_commands(self):
        vars = self.get_active_vars()
        if not vars:
            return "# No active project set."
        
        commands = []
        for key, value in vars.items():
            commands.append(f'export {key}="{value}"')
        return "\n".join(commands)

    def delete_project(self, name):
        data = self._load_data()
        if name in data["projects"]:
            del data["projects"][name]
            if data.get("active") == name:
                data["active"] = None
            self._save_data(data)
            return True
        return False

def main():
    import sys
    vault = VaultManager()
    
    if len(sys.argv) < 2:
        print("Usage: envoy [list|switch|add|export|delete] [args]")
        return

    cmd = sys.argv[1]

    if cmd == "list":
        projects = vault.list_projects()
        print("Projects:", ", ".join(projects) if projects else "None")
    
    elif cmd == "switch" and len(sys.argv) > 2:
        if vault.switch_project(sys.argv[2]):
            print(f"Switched to {sys.argv[2]}")
        else:
            print("Project not found.")
            
    elif cmd == "export":
        print(vault.export_shell_commands())
        
    elif cmd == "add" and len(sys.argv) > 2:
        name = sys.argv[2]
        vars = {}
        print("Enter variables (key=value). Type 'done' to finish:")
        while True:
            line = input("> ")
            if line.lower() == 'done': break
            if '=' in line:
                k, v = line.split('=', 1)
                vars[k] = v
        vault.add_project(name, vars)
        print(f"Project {name} saved.")

    elif cmd == "delete" and len(sys.argv) > 2:
        if vault.delete_project(sys.argv[2]):
            print(f"Deleted {sys.argv[2]}")
        else:
            print("Project not found.")

if __name__ == "__main__":
    main()