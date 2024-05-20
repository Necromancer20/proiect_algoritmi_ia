import sys
from gui.gui_main import tkinter_menu
from cli.cli_main import cli_menu

def main():
    """
    Display the main menu, allowing the user to choose between CLI and Tkinter interfaces.
    """
    print("Choose interface:")
    print("1. CLI")
    print("2. GUI")
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        from cli import cli_main
        cli_main.cli_menu()
    elif choice == "2":
        from gui import gui_main
        gui_main.tkinter_menu()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
