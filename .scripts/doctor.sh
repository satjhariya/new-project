#!/usr/bin/env bash

set -e

echo "======================================="
echo " Engineering MCP Suite - Doctor"
echo "======================================="
echo

check_command() {
    if command -v "$1" >/dev/null 2>&1; then
        printf "✅ %-25s %s\n" "$1" "$(command -v "$1")"
    else
        printf "❌ %-25s Not Found\n" "$1"
    fi
}

check_directory() {
    if [ -d "$1" ]; then
        printf "✅ %-25s Present\n" "$1"
    else
        printf "❌ %-25s Missing\n" "$1"
    fi
}

check_file() {
    if [ -f "$1" ]; then
        printf "✅ %-25s Present\n" "$1"
    else
        printf "❌ %-25s Missing\n" "$1"
    fi
}

echo "Tools"
echo "---------------------------------------"

check_command python3
check_command uv
check_command git

echo
echo "Versions"
echo "---------------------------------------"

python3 --version || true
uv --version || true
git --version || true

echo
echo "Project Structure"
echo "---------------------------------------"

check_directory src
check_directory tests
check_directory docs
check_directory scripts

check_file pyproject.toml
check_file README.md

echo
echo "Virtual Environment"
echo "---------------------------------------"

if [ -d ".venv" ]; then
    echo "✅ .venv found"
else
    echo "❌ .venv missing"
fi

echo
echo "Python Package Checks"
echo "---------------------------------------"

uv run python -c "import mcp; print('✅ mcp:', mcp.__file__)" 2>/dev/null || echo "❌ mcp not installed"

uv run python -c "import pydantic; print('✅ pydantic:', pydantic.__version__)" 2>/dev/null || echo "❌ pydantic not installed"

echo
echo "Import Test"
echo "---------------------------------------"

uv run python -c "import ai_rf_system; print('✅ ai_rf_system import successful')" 2>/dev/null || echo "❌ engineering_mcp import failed"

echo
echo "======================================="
echo " Doctor completed."
echo "======================================="