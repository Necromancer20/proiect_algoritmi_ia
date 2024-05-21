import sys
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning
from handlers import (
    regine_backtracking_handler,
    regine_alpinist_handler,
    regine_simulated_annealing_handler,
    regine_genetic_handler,
    tsp_backtracking_handler,
    tsp_nearest_neighbor_handler,
)
from utils.utils import (
    info_gui,
    exit
)

# Mapping of menu options to their corresponding functions
option_to_func = {
    "a": regine_backtracking_handler.handle_gui,
    "b": regine_alpinist_handler.handle_gui,
    "c": regine_simulated_annealing_handler.handle_gui,
    "d": regine_genetic_handler.handle_gui,
    "e": None,  # Placeholder for plot functions
    "f": tsp_backtracking_handler.handle_gui,
    "g": tsp_nearest_neighbor_handler.handle_gui,
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
    "h": "Plotare grafice problema comis-voiajorului"
}

# Board sizes for the chessboard problems
board_sizes = [3, 5, 15, 30]



def tkinter_menu():
    def update_second_combobox(option):
        """
        Updates the second combobox values based on the selected option.

        Args:
            option: The selected option from the first combobox.
        """
        if option in ["a", "b", "c", "d"]:
            option_combobox_2["values"] = board_sizes + ["export"]
        elif option in ["f", "g"]:
            option_combobox_2["values"] = ["export"]
        else:
            option_combobox_2["values"] = []

    def execute_option():
        """
        Executes the selected option.
        """
        selected_index = option_combobox_1.current()
        if selected_index != -1:
            option = list(menu_options.keys())[selected_index]
            handler_function = option_to_func.get(option)
            if handler_function:
                if option in ["a", "b", "c", "d"]:
                    size_index = option_combobox_2.current()
                    if size_index != -1:
                        size = board_sizes[size_index]
                        handler_function(subframe, size)
                    else:
                        showwarning("Warning", "Please select a board size.")
                else:
                    handler_function(subframe)
            else:
                showwarning("Warning", "This option is not implemented yet.")

    def on_option_select(event):
        """
        Handles the event when an option is selected from the first combobox.

        Args:
            event: The event object.
        """
        selected_index = option_combobox_1.current()
        if selected_index != -1:
            option = list(menu_options.keys())[selected_index]
            update_second_combobox(option)
            if option_combobox_2["values"]:
                option_combobox_2.set(option_combobox_2["values"][0])
                option_combobox_2.pack()
            else:
                option_combobox_2.set("")
                option_combobox_2.pack()

    # Create the main tkinter window
    window = tk.Tk()
    window.title("Aplicatie IA")

    # Create a frame to hold the dropdowns
    dropdown_frame = tk.Frame(window)
    dropdown_frame.pack(side=tk.TOP, fill=tk.X)
    separator_frame = tk.Frame(window)
    separator_frame.pack(side=tk.TOP, fill=tk.X)

    # Create the first Combobox
    selected_option_1 = tk.StringVar()
    option_combobox_1 = ttk.Combobox(dropdown_frame, textvariable=selected_option_1, state="readonly", height=5)
    option_combobox_1.pack(side=tk.LEFT, padx=(10, 5), pady=5, fill=tk.X, expand=True)
    option_combobox_1["values"] = list(menu_options.values())
    option_combobox_1.bind("<<ComboboxSelected>>", on_option_select)

    # Create the second Combobox
    selected_option_2 = tk.StringVar()
    option_combobox_2 = ttk.Combobox(dropdown_frame, textvariable=selected_option_2, state="readonly", height=5)
    option_combobox_2.pack(side=tk.LEFT, padx=(5, 10), pady=5, fill=tk.X, expand=True)

    # Create a "Run" button
    run_button = tk.Button(dropdown_frame, text="Run", command=execute_option)
    run_button.pack(side=tk.LEFT, padx=(5, 10), pady=5, fill=tk.X, expand=True)

    # Separator between options and buttons
    sep = ttk.Separator(separator_frame, orient='horizontal')
    sep.pack(side=tk.BOTTOM, fill='x')

    # Placeholder for additional options
    subframe = tk.Frame(window)
    subframe.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Separator between options and buttons
    sep1 = ttk.Separator(button_frame, orient='horizontal')
    sep1.pack(side=tk.TOP, fill='x')

    # Info button
    info_button = tk.Button(button_frame, text="Info", command=info_gui)
    info_button.pack(side=tk.LEFT, padx=(10, 5), pady=5)

    # Exit button
    exit_button = tk.Button(button_frame, text="Exit", command=exit)
    exit_button.pack(side=tk.RIGHT, padx=(5, 10), pady=5)

    state = not window.attributes('-fullscreen')
    window.attributes('-fullscreen', state)

    def focus_window():
        window.focus_force()

    # Focus on the window after opening
    window.after(100, focus_window)

    # Start the main event loop
    window.mainloop()
