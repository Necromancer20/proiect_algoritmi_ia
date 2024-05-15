import time

from algorithms.regine_backtracking import regine_backtracking
from constants import problem_file_paths
from functions.utils import read_board, print_board


def show_regine_backtracking_option() -> None:
    for path in problem_file_paths:
        board = read_board(path)

        start_time = time.time()
        solution = regine_backtracking(board)
        end_time = time.time()

        print(f"Solution found in {end_time - start_time:.2f} seconds.")
        print("Initial board:\n")
        print_board(board)
        print("Solved board:\n")
        print_board(solution)
