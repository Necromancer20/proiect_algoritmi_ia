import tkinter as tk
from tkinter import ttk
import networkx as nx
import random, sys, timeit, os
from tkinter.messagebox import showinfo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from algorithms import (
    queens_backtracking,
    queens_genetic,
    queens_hill_climbing,
    queens_simulated_annealing,
    tsp_backtracking,
    tsp_nearest_neighbor,
)

import utils.constants

def draw_board_solution(solution, parent_frame):
    max_board_size = 600
    board_size = len(solution)
    square_size = max_board_size // board_size
    font_size = square_size // 2

    for row in range(board_size):
        for col in range(board_size):
            color = "white" if (row + col) % 2 == 0 else "gray"
            square = tk.Frame(parent_frame, bg=color, width=square_size, height=square_size)
            square.grid(row=row, column=col)

            if solution[row][col] == 1:
                label = tk.Label(square, text="Q", font=("Helvetica", font_size), bg=color)
                label.place(relx=0.5, rely=0.5, anchor="center")

def read_board(input_file_path: str) -> list[list[int]]:
    board = []

    with open(input_file_path, 'r') as file:
        for line in file:
            board.append(
                list(
                    map(int, list(line.strip()))
                )
            )

    return board

def generate_random_board(n: int) -> list[list[int]]:
    """
    Generates a random N x N chessboard with N queens placed randomly.

    Args:
        n: The size of the board (N).
        
    Returns:
        A 2D list representing the chessboard with N queens placed randomly.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Place N queens randomly on the board
    queens_positions = random.sample(range(n * n), n)
    
    for pos in queens_positions:
        row = pos // n
        col = pos % n
        board[row][col] = 1
    
    # Step 1: Ensure one queen per column
    board = shift_queens_horizontally(board)

    # Step 2: Ensure one queen per row
    board = shift_queens_vertically(board)

    return board

def info_gui() -> None:
    """
    Displays an information message box.
    """
    showinfo(title='Information', message=f"Made by Cyberus:\n=>Roman Petrica,\n=>Vizitiu Valentin,\n=>Canevschii Daniel")

def exit() -> None:
    """
    Exits the application.
    """
    sys.exit()

def count_attacks(board):
    attacks = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in range(i + 1, len(board)):
                    if board[k][j] == 1:
                        attacks += 1
                for k in range(len(board)):
                    if board[i][k] == 1 and j != k:
                        attacks += 1
                    if i + j == k + j and i != k:
                        attacks += 1
                    if i - j == k - j and i != k:
                        attacks += 1
    return attacks

def tournament_selection(population, n):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x[1])

def generate_random_distances(n_cities):
    # Generate a square matrix of random distances
    distances = [[0] * n_cities for _ in range(n_cities)]

    for i in range(n_cities):
        for j in range(i+1, n_cities):
            distances[i][j] = distances[j][i] = random.randint(1, 100)

    #np.fill_diagonal(distances, 0)  # Diagonal elements represent the distance from a city to itself, which is 0
    return distances#.tolist()

def draw_network(distances, optimal_path, start_node, path_found_net_frame):
    plt.clf()

    # Create a graph
    G = nx.Graph()

    # Add edges and nodes (based on the provided matrix)
    edges = []
    for i in range(len(distances)):
        for j in range(i+1, len(distances[0])):
            edge = (i, j, {'weight': distances[i][j]})
            edges.append(edge)

    G.add_edges_from(edges)
    
    path_tuple = []
    for i in range(len(optimal_path)-1):
        path_tuple.append((optimal_path[i], optimal_path[i+1]))

    # Define edge colors
    edge_colors = ['blue' if (u, v) in path_tuple or (v, u) in path_tuple else 'black' for u, v, _ in G.edges(data=True)]

    # Define node colors
    node_colors = ['red' if node == start_node else 'skyblue' for node in G.nodes()]

    # Plot the graph
    pos = nx.spring_layout(G)  # Layout algorithm for positioning nodes
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=12, font_weight='bold', edge_color=edge_colors)

    # Add edge labels
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Show the plot
    plt.title("Traveling Salesman Problem Graph")
    plt.axis('off')  # Hide axis

    # Embed the plot in tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=path_found_net_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def export_all() -> None:
    export_timing(queens_backtracking.solve_queens_backtracking, utils.constants.queen_algos_entries)
    export_timing(queens_hill_climbing.solve_queens_hill_climbing, utils.constants.queen_algos_entries)
    export_timing(queens_genetic.solve_queens_genetic, utils.constants.queen_algos_entries)
    export_timing(queens_simulated_annealing.solve_queens_simulated_annealing, utils.constants.queen_algos_entries)
    export_timing(tsp_backtracking.solve_tsp_backtracking, utils.constants.tsp_backtracking)
    export_timing(tsp_nearest_neighbor.solve_tsp_nearest_neighbor, utils.constants.tsp_nearest_neighbor)

def export_timing(handler_function, sizes):
    results = {}
    for size in sizes:
        _, elapsed_time, _ = run_regine(handler_function, size)
        results[size] = elapsed_time
    with open(f"output_data/{handler_function.__name__}_results.txt", "w") as file:
        for size, result in results.items():
            file.write(f"{size} : {result:.8f}\n")

def run_regine(func_handler, size):
    board = generate_random_board(size)

    # Measure the time elapsed for executing the function
    start_time = timeit.default_timer()
    solution = func_handler(board)
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time

    return solution, elapsed_time, board

def run_tsp(func_handler, n_cities):
    distances = generate_random_distances(n_cities)

    start_city = random.randint(0, n_cities-1)

    start_time = timeit.default_timer()
    min_cost, optimal_path = func_handler(distances, start_city)
    end_time = timeit.default_timer()
    elapsed_time = end_time - start_time

    return min_cost, optimal_path, elapsed_time, distances, start_city

def parse_files_in_folder(folder_path, keyword, delimiter):
    result = {}
    
    # Iterate over each file in the given folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Check if the file name contains the keyword
            if keyword in file:
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.readlines()
                    # Parse each line by the delimiter and store the result
                    parsed_lines = [line.strip().split(delimiter) for line in content]
                    result[file.split(".")[0]] = parsed_lines
    
    return result

def display_matrix_with_borders(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        print("Empty matrix")
        return

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    col_widths = [max(len(str(matrix[i][j])) for i in range(num_rows)) for j in range(num_cols)]

    top_bottom_border = '+' + '+'.join(['-' * (col_width + 2) for col_width in col_widths]) + '+'
    middle_border = '|' + '+'.join(['-' * (col_width + 2) for col_width in col_widths]) + '|'

    print(top_bottom_border)

    for i in range(num_rows):
        row_str = '|'
        for j in range(num_cols):
            row_str += f" {matrix[i][j]:{col_widths[j]}} |"
        print(row_str)
        if i != num_rows - 1:
            print(middle_border)

    print(top_bottom_border)


def shift_queens_horizontally(board):
    n = len(board)
    
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                # Check the entire column for other queens
                conflict_found = any(board[r][col] == 1 for r in range(n) if r != row)
                
                if conflict_found:
                    # Shift the current queen to the right
                    new_col = (col + 1) % n
                    while board[row][new_col] == 1:
                        new_col = (new_col + 1) % n
                    # Move the queen
                    board[row][col] = 0
                    board[row][new_col] = 1
                    # After moving, re-check the new column for conflicts
                    col = new_col  # Update col to new_col to continue checking for conflicts
                    conflict_found = any(board[r][col] == 1 for r in range(n) if r != row)
                    while conflict_found:
                        # Shift to the next column
                        new_col = (new_col + 1) % n
                        while board[row][new_col] == 1:
                            new_col = (new_col + 1) % n
                        # Move the queen again
                        board[row][col] = 0
                        board[row][new_col] = 1
                        col = new_col  # Update col to new_col to continue checking for conflicts
                        conflict_found = any(board[r][col] == 1 for r in range(n) if r != row)

    return board

def shift_queens_vertically(board):
    n = len(board)
    
    for col in range(n):
        for row in range(n):
            if board[row][col] == 1:
                # Check the entire row for other queens
                conflict_found = any(board[row][c] == 1 for c in range(n) if c != col)
                
                if conflict_found:
                    # Shift the current queen downward
                    new_row = (row + 1) % n
                    while board[new_row][col] == 1:
                        new_row = (new_row + 1) % n
                    # Move the queen
                    board[row][col] = 0
                    board[new_row][col] = 1
                    # After moving, re-check the new row for conflicts
                    row = new_row  # Update row to new_row to continue checking for conflicts
                    conflict_found = any(board[row][c] == 1 for c in range(n) if c != col)
                    while conflict_found:
                        # Shift to the next row
                        new_row = (new_row + 1) % n
                        while board[new_row][col] == 1:
                            new_row = (new_row + 1) % n
                        # Move the queen again
                        board[row][col] = 0
                        board[new_row][col] = 1
                        row = new_row  # Update row to new_row to continue checking for conflicts
                        conflict_found = any(board[row][c] == 1 for c in range(n) if c != col)

    return board