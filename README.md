# Project Template

This repository serves as a generic, batteries-included Python project skeleton. It is designed to be fully decoupled from any specific project name, meaning you can clone this setup and immediately begin building without needing to rewrite configuration files or build scripts.

## 🚀 Getting Started

### 1. Clone the Template
Clone this repository to your local machine:
```bash
git clone https://github.com/satjhariya/new-project.git 
cd new-project
```

### 2. Rename Project References
The setup is highly generic, so you only need to change a few things:
1. Open `pyproject.toml` and update the `name`, `version`, and `description` fields.
2. Rename the source package directory in `src/` to match your new project name (e.g., `src/new_project/`).

### 3. Setup the Environment
The project includes automated setup scripts that will initialize a virtual environment, sync dependencies, and run initial checks:

**On Linux/macOS:**
```bash
./.scripts/setup.sh
```

**On Windows:**
```bat
.\.scripts\setup.bat
```

## 📂 Project Structure Guide

Here is a guide to what each file and directory is supposed to do. As a new developer, use this to navigate the boilerplate:

*   **`src/`**: Your main application code goes here. The internal folder is your primary Python package.
    *   `__main__.py`: The primary entry point for the application. Start building your app's main execution flow here.
*   **`tests/`**: Contains your `pytest` test suite.
    *   `test_main.py`: A placeholder test file. Add more test files prefixed with `test_` as you build out functionality.
*   **`docs/`**: Documentation folder.
    *   *Fill out the markdown files in here (e.g., `architecture.md`, `decision.md`) as your project evolves to maintain a record of design choices.*
*   **`.scripts/`**: Automation scripts.
    *   `build_exe.py`: Dynamically discovers your project name and compiles a standalone executable using PyInstaller.
    *   `run.py`: A generic runner that dynamically finds your package in `src/` and executes it.
    *   `clean_build`, `clear_caches`, `doctor`, `setup`: Utility scripts for project maintenance (provided in both `.sh` and `.bat`).
*   **`.vscode/`**: VS Code configuration files.
    *   `tasks.json`: Contains pre-configured commands to run tests, format code, check types, and build the executable.
    *   `launch.json`: Pre-configured debugger for running your app.
*   **`specs/`**:
    *   `app.spec`: A generic PyInstaller specification file used for building the executable.
*   **`pyproject.toml`**: The main configuration file. It manages dependencies (via `uv`), tools like `ruff` (formatting/linting), `pytest` (testing), and `pyrefly` (type checking).

## 🛠️ Developer Commands (VS Code)

This template heavily utilizes VS Code tasks. Press `Ctrl+Shift+B` (or `Cmd+Shift+B` on macOS) to access the build menu, or run them from the command palette (`Tasks: Run Task`):

*   **`▶️ Run Application`**: Executes the generic app runner (`.scripts/run.py`).
*   **`🧪 Run Tests`**: Executes the test suite via `pytest`.
*   **`🎨 Ruff: Format`**: Formats the codebase.
*   **`🚀 Full Validation Pipeline`**: Runs dependencies sync, formatting, type checking, and tests in sequence.
*   **`📦 Generate Executable`**: Compiles the source code into a standalone binary inside the `dist/` folder.
