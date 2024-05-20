import tkinter as tk
from tkinter import ttk
from algorithms.regine_backtracking import solve_n_queens_backtracking

def handle_cli():
    print("Executing Backtracking for N-Queens problem...")
    size = int(input("Enter the size of the board (N): "))
    board = [[0] * size for _ in range(size)]
    solution, duration = solve_n_queens_backtracking(board)
    print(f"Solution:\n{solution}")
    print(f"Duration: {duration:.4f} seconds")

def handle_gui(window):
    def run_algorithm():
        size = int(size_entry.get())
        board = [[0] * size for _ in range(size)]
        solution, duration = solve_n_queens_backtracking(board)
        result_text.delete("1.0", tk.END)  # Clear previous results
        result_text.insert(tk.END, f"Solution:\n{solution}\n")
        result_text.insert(tk.END, f"Duration: {duration:.4f} seconds")

    # Create GUI elements
    label = tk.Label(window, text="Enter the size of the board (N):")
    label.pack()

    size_entry = tk.Entry(window)
    size_entry.pack()

    execute_button = tk.Button(window, text="Execute", command=run_algorithm)
    execute_button.pack()

    result_text = tk.Text(window, height=10, width=50)
    result_text.pack()

    window.mainloop()

