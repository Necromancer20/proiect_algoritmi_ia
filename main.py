import os
import tkinter as tk
from tkinter import ttk
from functions import (
    comis_voiajor_apropiat_vecin_option,
    comis_voiajor_bkt_rec_option,
    comis_voiajor_plot_option,
    info_option,
    invalid_option,
    n_regine_plot_option,
    regine_alpinist_option,
    regine_backtracking_option,
    regine_genetic_algorithm_option,
    regine_simulated_annealing_option,
)


option_to_func = {
    "a": regine_backtracking_option.show_regine_backtracking_option,
    "b": regine_alpinist_option.show_regine_alpinist_option,
    "c": regine_simulated_annealing_option.show_simulated_annealing_option,
    "d": regine_genetic_algorithm_option.show_genetic_algorithm_option,
    "e": n_regine_plot_option.show_n_regine_plot,
    "f": comis_voiajor_bkt_rec_option.show_tsp_recursive_backtracking_option,
    "g": comis_voiajor_apropiat_vecin_option.show_tsp_nearest_neighbor_option,
    "h": comis_voiajor_plot_option.show_comis_voiajor_regine_plot,
    "x": info_option.show_info,
    "y": exit,
}

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
    while True:
        os.system("cls")
        print(menu_options)
        print("Input option:\n>>>")
        option = input().lower()

        try:
            option_to_func.get(option, invalid_option.show_invalid_option)()
        except Exception as e:
            print(f"An error occurred: {e}")


def tkinter_menu():
    # The main tkinter window
    window = tk.Tk()

    # setting the title and
    window.title("Aplicatie IA")

    # Calculate the required height based on the number of buttons
    button_height = 25  # Height of each button
    num_buttons = len(menu_options)
    window_height = num_buttons * (button_height + 10)  # Add spacing between buttons

    # Set the window dimensions
    window_width = 500
    window.geometry(f"{window_width}x{window_height}")
    window.update()    
    
    # Define a function to execute when a button is clicked
    def execute_option(option):
        option_to_func.get(option, invalid_option.show_invalid_option)()

    # Create buttons for each option with corresponding text
    for option, text in menu_options.items():
        option_button = ttk.Button(master=window, text=text, command=lambda opt=option: execute_option(opt))
        option_button.pack(side=tk.TOP, padx=10, pady=5, anchor="w", fill=tk.X)

    # run the gui
    window.mainloop()


def main_menu():
    # cli_menu()
    tkinter_menu()


if __name__ == "__main__":
    main_menu()
