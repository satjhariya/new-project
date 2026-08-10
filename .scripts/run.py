#!/usr/bin/env python3
import runpy
import sys
from pathlib import Path


def main():
    src_dir = Path("src")
    if not src_dir.exists():
        print("Error: src/ directory not found.")
        sys.exit(1)

    packages = [d for d in src_dir.iterdir() if d.is_dir() and (d / "__init__.py").exists()]
    if not packages:
        print("Error: No valid Python package found in src/")
        sys.exit(1)

    package_name = packages[0].name
    print(f"Starting package: {package_name}")
    runpy.run_module(package_name, run_name="__main__")


if __name__ == "__main__":
    main()
