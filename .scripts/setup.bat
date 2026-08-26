@echo off

echo =======================================
echo Project Setup
echo =======================================

echo.
echo Checking Python...
python --version

echo.
echo Checking uv...
uv --version

echo.
echo Creating virtual environment...
uv venv

echo.
echo Synchronizing dependencies...
uv sync

echo.
echo Running Ruff...
uv run ruff check .

echo.
echo Running pyrefly...
uv run pyrefly check

echo.
echo Running tests...
uv run pytest

echo.
echo Setup completed successfully.