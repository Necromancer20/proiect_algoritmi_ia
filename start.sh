#!/bin/bash
# Bash script to install dependencies, set up virtual environment, activate it, and run main.py

# Set up virtual environment
echo "Setting up virtual environment..."
python -m venv .env > /dev/null 2>&1 || {
    echo "Error: Failed to set up virtual environment."
    exit 1
}

# Activate the virtual environment
echo "Activating virtual environment..."
source ./.env/bin/activate > /dev/null 2>&1 || {
    echo "Error: Failed to activate virtual environment."
    exit 1
}

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1 || {
    echo "Error: Failed to install dependencies."
    exit 1
}

# Run main.py
echo "Running main.py..."
python main.py
if [ $? -ne 0 ]; then
    echo "Error: Failed to run main.py."
    exit 1
fi

# Log success message
echo "Success: All steps completed successfully."

# Pause to keep the terminal window open
read -p "Press any key to exit..."
