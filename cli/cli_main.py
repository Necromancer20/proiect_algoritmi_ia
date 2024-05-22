import os,sys
from handlers import (
    queens_backtracking_handler,
    queens_genetic_handler,
    queens_hill_climbing_handler,
    queens_simulated_annealing_handler,
    tsp_backtracking_handler,
    tsp_nearest_neighbor_handler,
)

# Mapping of menu options to their corresponding functions
option_to_func = {
    "a": queens_backtracking_handler.handle_cli,
    "b": queens_hill_climbing_handler.handle_cli,
    "c": queens_simulated_annealing_handler.handle_cli,
    "d": queens_genetic_handler.handle_cli,
    "e": tsp_backtracking_handler.handle_cli,
    "f": tsp_nearest_neighbor_handler.handle_cli,
}

# Mapping of menu options to their corresponding display text
menu_options = {
    "a": "Problema celor N regine (backtracking recursiv)",
    "b": "Problema celor N regine (alg. alpinistului)",
    "c": "Problema celor N regine (alg. calirii simulate)",
    "d": "Problema celor N regine (alg. genetic)",
    "e": "Problema comis-voiajorului (backtracking recursiv)",
    "f": "Problema comis-voiajorului (alg. celui mai apropiat vecin)",
    "x": "Info",
    "y": "Exit",
}

def cli_menu():
    """
    Display the command-line interface menu, allowing users to interact via the console.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        # Display menu options
        for option, text in menu_options.items():
            print(f"{option} : {text}")

        # Prompt for user input
        print("\nInput option:\n>>>", end=" ")
        option = input().strip().lower()

        if option == "x":
            show_info_cli()
        elif option == "y":
            exit() # Here the application exits
        else:
            try:
                func_handler = option_to_func.get(option)
                if func_handler is None:
                    raise Exception("Choose a valid option")
                size = int(input("\nInput a size : "))
                if(size <= 2):
                    raise Exception("Size not accepted")
                # Execute the selected option
                func_handler(size)
            except Exception as e:
                # Handle errors gracefully
                print(f"An error occurred: {e}")

        input("Press Enter to continue...")

def show_info_cli() -> None:
    print(
        """\
Nume echipa: Cyberus
    - Roman Petrica
    - Canevschii Daniel
    - Vizitiu Valentin
"""
    )

def exit() -> None:
    sys.exit()