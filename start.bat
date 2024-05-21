@echo off
rem Batch script to run main.py using Python in a terminal window

rem Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not found on PATH.
    exit /b 1
)

rem Run main.py in a terminal window
start cmd /k "python main.py"
