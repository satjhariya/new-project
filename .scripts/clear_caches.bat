@echo off
echo Clearing Python caches...

for /d /r %%d in (
    __pycache__
    .pytest_cache
    .ruff_cache
    .mypy_cache
    .hypothesis
    .tox
) do (
    if exist "%%d" rd /s /q "%%d"
)

del /s /q *.pyc 2>nul
del /s /q *.pyo 2>nul

echo Done.