import tkinter as tk
import random

def draw_board_solution(solution, parent_frame):
    colors = ["white", "gray"]
    max_board_size = 600
    for row in range(len(solution)):
        for col in range(len(solution[0])):
            color = colors[(row + col) % 2]
            square = tk.Frame(parent_frame, bg=color, width=max_board_size/len(solution), height=max_board_size/len(solution))
            square.grid(row=row, column=col)

            if solution[row][col] == 1:
                label = tk.Label(square, text="Q", font=("Helvetica", 12))
                label.pack()

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