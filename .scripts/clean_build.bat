@echo off
echo Cleaning build artifacts...

if exist build rd /s /q build
if exist dist rd /s /q dist
if exist htmlcov rd /s /q htmlcov
if exist .coverage del /q .coverage

for /d %%d in (*.egg-info) do (
    rd /s /q "%%d"
)

echo Done.