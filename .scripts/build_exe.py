#!/usr/bin/env python3
"""
Build executable using PyInstaller (Generic).
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = PROJECT_ROOT / "build"
DIST_DIR = PROJECT_ROOT / "dist"


def get_project_name() -> str:
    with open(PROJECT_ROOT / "pyproject.toml", "rb") as f:
        config = tomllib.load(f)
    return config.get("project", {}).get("name", "app-executable")


def get_spec_file() -> Path:
    specs_dir = PROJECT_ROOT / "specs"
    spec_files = list(specs_dir.glob("*.spec"))
    if not spec_files:
        raise FileNotFoundError("No .spec file found in specs/")
    return spec_files[0]


def get_package_main() -> Path:
    src_dir = PROJECT_ROOT / "src"
    packages = [d for d in src_dir.iterdir() if d.is_dir() and (d / "__init__.py").exists()]
    if not packages:
        raise FileNotFoundError("No valid Python package found in src/")
    return packages[0] / "__main__.py"


def validate(spec_file: Path, main_file: Path) -> None:
    required = (
        PROJECT_ROOT / "pyproject.toml",
        PROJECT_ROOT / "README.md",
        main_file,
        spec_file,
    )
    missing = [path for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing required files:\n" + "\n".join(str(path) for path in missing)
        )


def clean() -> None:
    for directory in (BUILD_DIR, DIST_DIR):
        if directory.exists():
            print(f"Removing {directory}")
            shutil.rmtree(directory)


def build(spec_file: Path) -> None:
    command = ["uv", "run", "pyinstaller", "--clean", "--noconfirm", str(spec_file)]
    subprocess.run(command, cwd=PROJECT_ROOT, check=True)


def verify(executable_name: str) -> None:
    executable = (
        DIST_DIR / f"{executable_name}.exe"
        if sys.platform.startswith("win")
        else DIST_DIR / executable_name
    )
    if not executable.exists():
        raise FileNotFoundError(f"Executable not generated:\n{executable}")

    print("\n" + "=" * 60)
    print(f" {executable_name} Build Successful")
    print("=" * 60)
    print(f"Executable : {executable}")
    print("=" * 60)


def main() -> None:
    print("=" * 60)
    print(" Generic Executable Build")
    print("=" * 60)

    try:
        project_name = get_project_name()
        spec_file = get_spec_file()
        main_file = get_package_main()

        validate(spec_file, main_file)
        clean()
        build(spec_file)
        verify(project_name)
    except Exception as e:
        print(f"Build failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
