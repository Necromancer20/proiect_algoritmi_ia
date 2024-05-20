import sys
import tkinter as tk
from tkinter import ttk, messagebox
from handlers import (
    regine_backtracking_handler,
    # regine_alpinist_handler,
    # regine_simulated_annealing_handler,
    # regine_genetic_handler,
    # tsp_backtracking_handler,
    # tsp_nearest_neighbor_handler,
    # show_info_handler
)

# Mapping of menu options to their corresponding functions
option_to_func = {
    "a": regine_backtracking_handler.handle_gui,
    # "b": regine_alpinist_handler.handle_gui,
    # "c": regine_simulated_annealing_handler.handle_gui,
    # "d": regine_genetic_handler.handle_gui,
    # "e": show_info_handler,  # Placeholder for plot functions
    # "f": tsp_backtracking_handler.handle_gui,
    # "g": tsp_nearest_neighbor_handler.handle_gui,
    # "h": show_info_handler,  # Placeholder for plot functions
    # "x": show_info_handler,
    "y": exit,
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

def tkinter_menu():
    """
    Display the Tkinter GUI menu, allowing users to interact with a Combobox.
    """
    window = tk.Tk()
    window.title("Aplicatie IA")

    button_height = 25
    num_buttons = len(menu_options)
    window_height = num_buttons * (button_height + 10)
    window_width = 500
    window.geometry(f"{window_width}x{window_height}")

    def execute_option(option):
        try:
            option_to_func.get(option, show_invalid_option)(window)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    selected_option = tk.StringVar()
    option_combobox = ttk.Combobox(window, textvariable=selected_option, state="readonly")
    option_combobox.pack(side=tk.TOP, padx=10, pady=5, anchor="w", fill=tk.X)
    option_combobox["values"] = list(menu_options.values())

    def on_combobox_select(event):
        selected_index = option_combobox.current()
        if selected_index != -1:
            option = list(menu_options.keys())[selected_index]
            execute_option(option)

    option_combobox.bind("<<ComboboxSelected>>", on_combobox_select)

    window.mainloop()



def show_invalid_option() -> None:
    pass

def exit() -> None:
    sys.exit()