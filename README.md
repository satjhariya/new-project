# new-project

A generic Python project template with environment-backed settings, configurable
logging, repeatable validation tasks, and optional PyInstaller packaging.

## 🚀 Getting Started

### 1. Clone the Template
Clone this repository to your local machine:
```bash
git clone https://github.com/satjhariya/new-project.git 
cd new-project
```

### 2. Configure the Template

Update the project metadata in `pyproject.toml` and replace `src/new_project/`
when adopting this template for a different package name. Keep the package
directory, build target, and discovery scripts aligned.

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

The main areas are:

*   **`src/`**: Your main application code goes here. The internal folder is your primary Python package.
    *   `__main__.py`: The primary entry point for the application. Start building your app's main execution flow here.
*   **`tests/`**: Contains your `pytest` test suite.
    *   `test_main.py`: A placeholder test file. Add more test files prefixed with `test_` as you build out functionality.
*   **`docs/`**: Architecture, development, conventions, decisions, roadmap, timeline, and changelog.
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

Run the VS Code tasks from the command palette (`Tasks: Run Task`):

*   **`▶️ Run Application`**: Executes the generic app runner (`.scripts/run.py`).
*   **`🧪 Run Tests`**: Executes the test suite via `pytest`.
*   **`🎨 Ruff: Format`**: Formats the codebase.
*   **`🚀 Full Validation Pipeline`**: Runs dependencies sync, formatting, type checking, and tests in sequence.
*   **`📦 Generate Executable`**: Compiles the source code into a standalone binary inside the `dist/` folder.

For environment variables, validation commands, platform notes, and troubleshooting, see the [Development Guide](docs/development.md).

By default, application logs are written to `logs/app.log` relative to the
process working directory. Set `LOG_FILE` in `.env` to change the location.

## Documentation

- [Architecture](docs/architecture.md)
- [Changelog](docs/CHANGELOG.md)
- [Conventions](docs/conventions.md)
- [Architectural Decisions](docs/decision.md)
- [Development Guide](docs/development.md)
- [Roadmap](docs/roadmap.md)
- [Timeline](docs/timeline.md)
