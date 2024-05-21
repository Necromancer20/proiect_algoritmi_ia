#!/bin/bash
# Bash script to run main.py using Python

# Check if Python is installed
if ! command -v python &> /dev/null
then
    echo "Python is not installed or not found on PATH."
    exit 1
fi

# Run main.py
python main.py
