# Contributing

Thank you for investing your time in contributing to our project!

## Development Setup

The project includes automated setup scripts that will initialize a virtual environment, sync dependencies, and run initial checks.

**On Linux/macOS:**
```bash
./.scripts/setup.sh
```

**On Windows:**
```bat
.\.scripts\setup.bat
```

## Making Changes

1. Fork the repository and create your branch from `main`.
2. Ensure you have run the setup scripts above.
3. Make your changes in the `src/` directory.

## Testing and Formatting

This project uses `pytest` for testing, `ruff` for formatting and linting, and `pyrefly` for type checking.

Before submitting a pull request, ensure all tests pass and code is correctly formatted.

From VS Code, you can run the following tasks:
*   **`🧪 Run Tests`**: Executes the test suite via `pytest`.
*   **`🎨 Ruff: Format`**: Formats the codebase.
*   **`🚀 Full Validation Pipeline`**: Runs dependencies sync, formatting, type checking, and tests in sequence.

## Submitting a Pull Request

1. Push your changes to your fork.
2. Open a Pull Request against the `main` branch of this repository.
3. Ensure the PR title clearly describes the change.
4. Fill out the PR template.
