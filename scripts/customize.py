#!/usr/bin/env python3
"""
Script to customize the project name from the template.
Caution - not tested extensively.

Usage: python scripts/customize.py new_project_name
"""

import os
import sys
import shutil
import tomli
import tomli_w
from pathlib import Path


def update_pyproject_toml(new_name: str):
    """Update pyproject.toml with the new project name."""
    toml_path = Path("pyproject.toml")
    with open(toml_path, "rb") as f:
        data = tomli.load(f)
    
    # Update project name
    data["project"]["name"] = new_name
    
    # Update scripts section to use new name
    if "project.scripts" in data:
        data["project.scripts"]["chat"] = f"scripts.chat:app"
    
    # Write back to file
    with open(toml_path, "wb") as f:
        tomli_w.dump(data, f)


def rename_example_dir(new_name: str):
    """Rename the example directory to the new project name."""
    if os.path.exists("example"):
        shutil.move("example", new_name)


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/customize.py new_project_name")
        sys.exit(1)
    
    new_name = sys.argv[1]
    
    # Validate project name (should be valid Python package name)
    if not new_name.isidentifier():
        print("Error: Project name must be a valid Python package name "
              "(alphanumeric and underscore characters only, cannot start with a number)")
        sys.exit(1)
    
    try:
        print(f"Customizing project for: {new_name}")
        
        # Update pyproject.toml
        update_pyproject_toml(new_name)
        print("✓ Updated pyproject.toml")
        
        # Rename example directory
        rename_example_dir(new_name)
        print(f"✓ Renamed 'example' directory to '{new_name}'")
        
        print("\nCustomization complete! Next steps:")
        print("1. Review the changes in pyproject.toml")
        print("2. Create a virtual environment: uv venv --python 3.11")
        print("3. Activate it: . ./.venv/bin/activate")
        print("4. Install dependencies: uv sync")
        
    except Exception as e:
        print(f"Error during customization: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()