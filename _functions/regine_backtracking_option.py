import time
import tkinter as tk
from tkinter import ttk
from constants import table_sizes
from algorithms.queens_backtracking import regine_backtracking
from functions.utils import read_board, print_board

def draw_solution(solution, window):
    colors = ["white", "gray"]
    maxSizeChessBoard = 750
    for row in range(len(solution)):
        for col in range(len(solution[0])):
            color = colors[(row + col) % 2]
            square = tk.Frame(window, bg=color, width=maxSizeChessBoard/len(solution), height=maxSizeChessBoard/len(solution))
            square.grid(row=row, column=col)

            if solution[row][col] == 1:
                label = tk.Label(square, text="Q", font=("Helvetica", 16))
                label.pack()

def solveQueenBacktracking(boardSize) -> None:
    board = [[0] * boardSize for _ in range(boardSize)]

    start_time = time.time()
    solution = regine_backtracking(board)
    end_time = time.time()
    
    # Create a Tkinter window
    window1 = tk.Tk()
    window1.title("Solution Chessboard")

    # Draw the solution chessboard
    draw_solution(solution, window1)
    
    print(f"Solution found in {end_time - start_time:.2f} seconds.")
    print("Solved board:\n")
    print_board(solution)

def chooseSizeWindow():
    # Create a Tkinter window
    chooseSize = tk.Tk()
    chooseSize.title("Choose Board Size")

    # Create buttons for each option with corresponding text
    for size in table_sizes:
        option_button = ttk.Button(master=chooseSize, text=f"{size}x{size}", command=lambda opt=size: solveQueenBacktracking(opt))
        option_button.pack(side=tk.TOP, padx=10, pady=5, anchor="w", fill=tk.X)


def show_regine_backtracking_option() -> None:
    chooseSizeWindow()
