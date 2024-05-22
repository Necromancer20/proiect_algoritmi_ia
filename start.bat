@echo off
rem Batch script to install dependencies, set up virtual environment, activate it, and run main.py

rem Set up virtual environment
echo Setting up virtual environment...
python -m venv .env > nul 2>&1 || (
    echo Error: Failed to set up virtual environment.
    exit /b 1
)

rem Activate the virtual environment
echo Activating virtual environment...
call .\.env\Scripts\activate.bat > nul 2>&1 || (
    echo Error: Failed to activate virtual environment.
    exit /b 1
)

rem Install dependencies
echo Installing dependencies...
pip install -r requirements.txt > nul 2>&1 || (
    echo Error: Failed to install dependencies.
    exit /b 1
)

rem Run main.py
echo Running main.py...
call python main.py
if %errorlevel% neq 0 (
    echo Error: Failed to run main.py.
    exit /b 1
)

rem Log success message
echo Success: All steps completed successfully.

rem Pause to keep the terminal window open
pause
