import tkinter as tk
from algorithms.queens_backtracking import solve_queens_backtracking
from utils.utils import (
    draw_board_solution,
    run_regine,
    display_matrix_with_borders
)

def handle_cli(size):
    if size <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    print(f"Executing Backtracking for N-Queens problem with size {size}...")

    solution, elapsed_time, _ = run_regine(solve_queens_backtracking, size)

    if solution is None:
        return

    print(f"Elapsed time: {elapsed_time:.10f} seconds")
    display_matrix_with_borders(solution)

def handle_gui(window, size):
    if size <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    solution, elapsed_time, _ = run_regine(solve_queens_backtracking, size)

    if solution is None:
        return

    # Clear the contents of the window
    for widget in window.winfo_children():
        widget.destroy()

    # Display the elapsed time
    time_label = tk.Label(window, text=f"Time elapsed: {elapsed_time:.8f} seconds")
    time_label.pack()

    # Create a frame for the chessboard
    chessboard_frame = tk.Frame(window)
    chessboard_frame.pack()

    # Draw the solution on the chessboard frame
    draw_board_solution(solution, chessboard_frame)

