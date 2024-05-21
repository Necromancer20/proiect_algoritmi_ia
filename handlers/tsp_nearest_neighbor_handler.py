import tkinter as tk
import timeit
from algorithms.regine_genetic import regine_genetic_algorithm
from utils.utils import (
    draw_board_solution,
    generate_random_board,
)

def handle_cli(size):
    if size <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    print(f"Executing Backtracking for N-Queens problem with size {size}...")

    board = generate_random_board(size)

    # Measure the time elapsed for executing the function
    start_time = timeit.default_timer()
    solution = regine_genetic_algorithm(board)
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time
    
    if solution is None:
        return

    print(f"Elapsed time: {elapsed_time:.10f} seconds")
    print(f"Solution:\n{solution}")

def handle_gui(window, size):
    if size <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    board = generate_random_board(size)

    # Measure the time elapsed for executing the function
    start_time = timeit.default_timer()
    solution = regine_genetic_algorithm(board)
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time

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
    draw_board_solution(board, input_chessboard_frame)

    # Create a frame for the chessboard
    result_chessboard_frame = tk.Frame(window)
    result_chessboard_frame.pack(side=tk.LEFT, padx=(10, 5), pady=5, fill=tk.X, expand=True)

    # Draw the solution on the chessboard frame
    draw_board_solution(solution, result_chessboard_frame)
