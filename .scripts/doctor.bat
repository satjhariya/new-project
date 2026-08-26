@echo off

echo =======================================
echo  Project Doctor
echo =======================================
echo.

echo Tools
echo ---------------------------------------

where python >nul 2>nul && (
    echo ✅ Python found
) || (
    echo ❌ Python not found
)

where uv >nul 2>nul && (
    echo ✅ uv found
) || (
    echo ❌ uv not found
)

where git >nul 2>nul && (
    echo ✅ Git found
) || (
    echo ❌ Git not found
)

echo.
echo Versions
echo ---------------------------------------

python --version
uv --version
git --version

echo.
echo Project Structure
echo ---------------------------------------

if exist src (
    echo ✅ src
) else (
    echo ❌ src
)

if exist tests (
    echo ✅ tests
) else (
    echo ❌ tests
)

if exist docs (
    echo ✅ docs
) else (
    echo ❌ docs
)

if exist .scripts (
    echo ✅ .scripts
) else (
    echo ❌ .scripts
)

if exist pyproject.toml (
    echo ✅ pyproject.toml
) else (
    echo ❌ pyproject.toml
)

if exist README.md (
    echo ✅ README.md
) else (
    echo ❌ README.md
)

echo.
echo Virtual Environment
echo ---------------------------------------

if exist .venv (
    echo ✅ .venv found
) else (
    echo ❌ .venv missing
)

echo.
echo Python Package Checks
echo ---------------------------------------

uv run python -c "import pydantic; print('✅ pydantic OK')" 2>nul || echo ❌ pydantic not installed

echo.
echo Import Test
echo ---------------------------------------

uv run python -c "from pathlib import Path; import importlib; packages = [path.name for path in Path('src').iterdir() if (path / '__init__.py').is_file()]; assert packages, 'No Python package found under src'; [importlib.import_module(package) for package in packages]; print('Package import successful:', ', '.join(packages))" 2>nul || echo Package import failed

echo.
echo =======================================
echo Doctor completed.
echo =======================================