import sys
from typing import NoReturn

# Import menus
from gui.gui_main import tkinter_menu
from cli.cli_main import cli_menu

# Constants for user choices
CLI_CHOICE = "1"
GUI_CHOICE = "2"
VALID_CHOICES = {CLI_CHOICE, GUI_CHOICE}


def display_menu() -> str:
    """
    Display the main menu and get the user's choice.

    Returns:
        str: The user's choice of interface.
    """
    print("Choose interface:")
    print(f"{CLI_CHOICE}. CLI")
    print(f"{GUI_CHOICE}. GUI")
    return input("Enter 1 or 2: ")


def handle_choice(choice: str) -> None:
    """
    Handle the user's menu choice and run the appropriate interface.

    Args:
        choice (str): The user's menu choice.
    """
    if choice == CLI_CHOICE:
        cli_menu()
    elif choice == GUI_CHOICE:
        tkinter_menu()
    else:
        raise ValueError("Invalid choice")


def main() -> None:
    """
    Display the main menu, allowing the user to choose between CLI and Tkinter interfaces.
    """
    while True:
        try:
            choice = display_menu()
            if choice in VALID_CHOICES:
                handle_choice(choice)
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ImportError as e:
            print(f"Error importing modules: {e}")
            sys.exit(1)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
