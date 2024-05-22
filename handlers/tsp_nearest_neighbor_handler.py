import tkinter as tk
from algorithms.tsp_nearest_neighbor import solve_tsp_nearest_neighbor
from utils.utils import (
    display_matrix_with_borders,
    draw_network,
    run_tsp
)

def handle_cli(n_cities):
    if n_cities <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    print(f"Executing nearest neighbor for TS problem with size {n_cities}...")

    min_cost, optimal_path, elapsed_time, distances, start_city = run_tsp(solve_tsp_nearest_neighbor, n_cities)

    print(f"Solution found in {elapsed_time:.8f} seconds.")

    if min_cost is not None:
        print(f"Initial distances:")
        display_matrix_with_borders(distances)

        print(f"Minimum cost for TSP starting from city {start_city}: {min_cost}")
        print("Optimal Path:")
        display_matrix_with_borders([optimal_path])
    else:
        print("No solution found.")

def handle_gui(window, n_cities=5):
    if n_cities <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    min_cost, optimal_path, elapsed_time, distances, start_city = run_tsp(solve_tsp_nearest_neighbor, n_cities)

    if min_cost is None:
        print("No solution found.")
        return

    # Clear the contents of the window
    for widget in window.winfo_children():
        widget.destroy()

    # Display the elapsed time
    time_label = tk.Label(window, text=f"Time elapsed: {elapsed_time:.8f} seconds")
    time_label.pack()

    # Create a frame for the chessboard
    path_found_net_frame = tk.Frame(window)
    path_found_net_frame.pack()

    # Draw the solution on the chessboard frame
    draw_network(distances, optimal_path, start_city, path_found_net_frame)
