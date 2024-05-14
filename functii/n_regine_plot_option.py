import time

from algoritmi.regine_alpinist import solve_regine_alpinist
from constants import problem_file_paths
from functii.utils import read_board, print_board
from plot.n_regine_plot import plot_chart


def show_n_regine_plot() -> None:
    print("Plotare grafice problema celor N regine")
    table_sizes = ['10x10', '20x20', '30x30', '40x40', '50x50']
   # table_sizes = ['8x8', '15x15', '26x26', '30x30', '42x42']
    solving_times = [2, 10, 20, 40, 60]
    # solving_times = [1, 5, 12, 27, 55]
   # solving_times_at = [1, 7, 10, 22, 40]
    solving_times_at = [3, 15, 30, 45, 60]
    algo_labels = ['Algorithm 1', 'Algorithm 2']  # Define labels for the algorithms
    plot_chart(table_sizes, solving_times, solving_times_at, algo_labels)
    input("Press Enter to continue...")