# Local Development Guide

## Environment Setup
Follow the instructions in the `README.md` to run the setup script. This will create your virtual environment and install all dependencies via `uv`.

## Running the Application
To run the application locally, use the VS Code task `▶️ Run Application`, or manually run:
```bash
uv run python .scripts/run.py
```

## Running Tests
Tests are located in the `tests/` directory and run via `pytest`.
```bash
uv run pytest
```
For coverage:
```bash
uv run pytest --cov=src
```

## Building the Executable
To build a standalone executable:
```bash
uv run python .scripts/build_exe.py
```
The output will be placed in the `dist/` folder.