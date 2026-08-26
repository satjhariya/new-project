# Conventions

## Source Layout

- Application code lives under `src/new_project/`.
- `src/new_project/__main__.py` is the executable module entry point.
- Shared configuration and logging are exported from `src/new_project/core/`.
- Tests live under `tests/` and follow `test_*.py` or `*_test.py` naming.
- Automation is kept under `.scripts/`; editor tasks and launchers are under
	`.vscode/`.

## Python and Tooling

- The supported Python version is 3.13 or newer.
- Ruff is configured for formatting and linting with a 100-character line length,
	double quotes, and import sorting.
- Pyrefly checks both `src` and `tests`; its configured platform is Windows and
	should be reviewed for cross-platform projects.
- pytest uses strict configuration and markers, with `unit`, `integration`, and
	`e2e` markers available.
- Formatting and linting are configured to allow automatic fixes.

## Naming

| Element | Convention |
| --- | --- |
| Variables and functions | `snake_case` |
| Classes | `PascalCase` |
| Constants | `UPPER_SNAKE_CASE` |
| Tests | `test_*.py`, `*_test.py`, and `test_*` functions |

## Configuration and Logging

Configuration uses Pydantic Settings and reads `.env` plus environment
variables. The settings cache should be cleared in tests when environment
values change. Logging is obtained through `get_logger()` and defaults to the
configured `DEFAULT_LOG_LEVEL`; use `shutdown_logging()` when tests need to
reset logging state.

## Git Workflow

The repository guidance recommends `feature/<feature-name>` and
`bugfix/<bug-name>` branch names and descriptive commits that explain why a
change was made. These conventions are documented guidance, not repository-
enforced hooks or CI checks.

## Open Policy Questions

- Should the Pyrefly platform be Linux, Windows, or a cross-platform setting?
- Should package discovery remain first-match based or become explicit?
- Which branch protection and CI rules, if any, should enforce the documented
	Git workflow?
