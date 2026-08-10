# -*- mode: python ; coding: utf-8 -*-
"""
Generic PyInstaller specification.
"""
import os
from pathlib import Path
try:
    import tomllib
except ImportError:
    import tomli as tomllib

PROJECT_ROOT = Path.cwd()

def get_project_info():
    with open(PROJECT_ROOT / "pyproject.toml", "rb") as f:
        config = tomllib.load(f)
    name = config.get("project", {}).get("name", "app-executable")
    
    src_dir = PROJECT_ROOT / "src"
    packages = [d for d in src_dir.iterdir() if d.is_dir() and (d / "__init__.py").exists()]
    main_file = packages[0] / "__main__.py" if packages else PROJECT_ROOT / "src" / "main.py"
    return name, main_file

project_name, ENTRY_POINT = get_project_info()
SRC_DIR = PROJECT_ROOT / "src"
README = PROJECT_ROOT / "README.md"

a = Analysis(
    [str(ENTRY_POINT)],
    pathex=[str(SRC_DIR)],
    binaries=[],
    datas=[(str(README), ".")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=project_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
)