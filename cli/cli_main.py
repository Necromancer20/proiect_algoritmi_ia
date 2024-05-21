import os,sys
from handlers import (
    regine_backtracking_handler,
    regine_alpinist_handler,
    regine_simulated_annealing_handler,
    regine_genetic_handler,
    tsp_backtracking_handler,
    tsp_nearest_neighbor_handler,
    show_info_handler
)

# Mapping of menu options to their corresponding functions
option_to_func = {
    "a": regine_backtracking_handler.handle_cli,
    "b": regine_alpinist_handler.handle_cli,
    "c": regine_simulated_annealing_handler.handle_cli,
    "d": regine_genetic_handler.handle_cli,
    #"e": queen_results_plot.draw_matplotlib_graph,  # Placeholder for plot functions
    #"f": tsp_backtracking_handler.handle_cli,
    #"g": tsp_nearest_neighbor_handler.handle_cli,
    "h": None,  # Placeholder for plot functions
}

# Mapping of menu options to their corresponding display text
menu_options = {
    "a": "Problema celor N regine (backtracking recursiv)",
    "b": "Problema celor N regine (alg. alpinistului)",
    "c": "Problema celor N regine (alg. calirii simulate)",
    "d": "Problema celor N regine (alg. genetic)",
    "e": "Plotare grafice problema celor N regine",
    "f": "Problema comis-voiajorului (backtracking recursiv)",
    "g": "Problema comis-voiajorului (alg. celui mai apropiat vecin)",
    "h": "Plotare grafice problema comis-voiajorului",
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
        option = input().lower()

        try:
            # Execute the selected option
            option_to_func.get(option, show_invalid_option)()
        except Exception as e:
            # Handle errors gracefully
            print(f"An error occurred: {e}")
        input("Press Enter to continue...")

def show_invalid_option() -> None:
    pass

def exit() -> None:
    sys.exit()