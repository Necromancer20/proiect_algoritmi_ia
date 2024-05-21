import tkinter as tk
import random, sys
from tkinter.messagebox import showinfo
from tkinter import ttk
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

    
