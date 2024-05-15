import time

from algorithms.regine_genetic_algorithm import regine_genetic_algorithm
from constants import problem_file_paths
from functions.utils import read_board, print_board


def show_genetic_algorithm_option() -> None:
    for path in problem_file_paths:
        board = read_board(path)
        start_time = time.time()
        solution = regine_genetic_algorithm(board)
        end_time = time.time()
        print(f"Genetic Algorithm Solution found in {end_time - start_time:.2f} seconds.")
        print(f"Initial board:\n")
        print_board(board)
        if solution is not None:
            print(f"Solved board:\n")
            print_board(solution)
        else:
            print("No solution found.")