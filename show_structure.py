import os

EXCLUDE_FOLDERS = {
    "venv", "__pycache__", "migrations", "node_modules", 
    ".git", ".idea", "site-packages", ".pytest_cache"
}
EXCLUDE_FILES = {
    "LICENSE", "README.md", ".gitignore", "pyproject.toml"
}

def print_tree(start_path, prefix=""):
    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        return

    for i, item in enumerate(entries):
        if item in EXCLUDE_FOLDERS or item in EXCLUDE_FILES:
            continue

        path = os.path.join(start_path, item)
        connector = "└── " if i == len(entries) - 1 else "├── "

        if os.path.isdir(path):
            print(prefix + connector + item + "/")
            print_tree(path, prefix + ("    " if i == len(entries) - 1 else "│   "))
        else:
            print(prefix + connector + item)

# Run the function
print_tree(".")
