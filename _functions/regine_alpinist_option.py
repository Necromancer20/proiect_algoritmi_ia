import time

from algorithms.regine_alpinist import solve_regine_alpinist
from constants import problem_file_paths
from functions.utils import read_board, print_board


def show_regine_alpinist_option() -> None:
    for path in problem_file_paths:
        board = read_board(path)

        start_time = time.time()
        solution = solve_regine_alpinist(board)
        end_time = time.time()

        print(f"Solution found in {end_time - start_time:.2f} seconds.")
        print(f"Initial board:\n")
        print_board(board)
        print(f"Solved board:\n")
        print_board(solution)
