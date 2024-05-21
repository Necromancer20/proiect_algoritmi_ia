import tkinter as tk
import timeit, random
from algorithms.tsp_backtracking import comis_voiajor_recursive_backtracking
from utils.utils import (
    draw_board_solution,
    generate_random_board,
    generate_random_distances,
    draw_network,
)

def handle_cli(n_cities):
    if n_cities <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    print(f"Executing Backtracking for TS problem with size {n_cities}...")

    distances = generate_random_distances(n_cities)

    start_city = random.randint(0, n_cities-1)

    start_time = timeit.default_timer()
    min_cost, optimal_path = comis_voiajor_recursive_backtracking(distances, start_city)
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time

    print(f"Solution found in {elapsed_time:.2f} seconds.")

    if min_cost is not None:
        print(f"Initial distances:\n")
        for row in distances:
            print(' '.join(map(str, row)))
        print(f"Minimum cost for TSP starting from city {start_city}: {min_cost}")
        print("Optimal Path:", optimal_path)
    else:
        print("No solution found.")


def handle_gui(window, n_cities=5):
    if n_cities <= 0:
        print("Invalid input size. Size must be a positive integer.")
        return

    distances = generate_random_distances(n_cities)

    start_city = random.randint(0, n_cities-1)

    # Measure the time elapsed for executing the function
    start_time = timeit.default_timer()
    min_cost, optimal_path = comis_voiajor_recursive_backtracking(distances, start_city)
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time


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
