import tkinter as tk
from algorithms.queens_genetic import solve_queens_genetic
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

    solution, elapsed_time, init_board = run_regine(solve_queens_genetic, size)

    if solution is None:
        return

    print(f"Elapsed time: {elapsed_time:.10f} seconds")

    print("\nStarting board:\n")
    display_matrix_with_borders(init_board)

    print("\nSolution board:\n")
    display_matrix_with_borders(solution)


def handle_gui(window, size):
    if size <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    solution, elapsed_time, init_board = run_regine(solve_queens_genetic, size)

    if solution is None:
        return

    # Clear the contents of the window
    for widget in window.winfo_children():
        widget.destroy()

    # Display the elapsed time
    time_label = tk.Label(window, text=f"Time elapsed: {elapsed_time:.8f} seconds")
    time_label.pack()

    # Create a frame for the chessboard
    input_chessboard_frame = tk.Frame(window)
    input_chessboard_frame.pack(side=tk.LEFT, padx=(10, 5), pady=5, fill=tk.X, expand=True)

    # Draw the solution on the chessboard frame
    draw_board_solution(init_board, input_chessboard_frame)

    # Create a frame for the chessboard
    result_chessboard_frame = tk.Frame(window)
    result_chessboard_frame.pack(side=tk.LEFT, padx=(10, 5), pady=5, fill=tk.X, expand=True)

    # Draw the solution on the chessboard frame
    draw_board_solution(solution, result_chessboard_frame)

