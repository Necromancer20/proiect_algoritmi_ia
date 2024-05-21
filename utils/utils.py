import tkinter as tk
import random, sys
from tkinter.messagebox import showinfo

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
    showinfo(title='Information', message=f"Made by:\n=>Roman Petrica,\n=>Vizitiu Valentin,\n=>Canevschii Daniel")

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