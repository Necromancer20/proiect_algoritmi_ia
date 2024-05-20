import tkinter as tk
import timeit
from algorithms.regine_backtracking import solve_n_queens_problem
from utils.utils import draw_board_solution

def handle_cli(size):
    if size <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    print(f"Executing Backtracking for N-Queens problem with size {size}...")

    # Measure the time elapsed for executing the function
    start_time = timeit.default_timer()
    solution = solve_n_queens_problem(size, size)
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

    # Measure the time elapsed for executing the function
    start_time = timeit.default_timer()
    solution = solve_n_queens_problem(size)
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
    chessboard_frame = tk.Frame(window)
    chessboard_frame.pack()

    # Draw the solution on the chessboard frame
    draw_board_solution(solution, chessboard_frame)

