import time
from typing import Callable

import matplotlib.pyplot as plt

from algorithms.queens_hill_climbing import solve_queens_hill_climbing
from algorithms.queens_backtracking import regine_backtracking
from algorithms.solve_queens_genetic import solve_queens_genetic
from algorithms.queens_simulated_annealing import solve_queens_simulated_annealing
from functions.utils import generate_board

TABLE_SIZES = (3, 5, 10, 12, 13, 15, 20)
ALGORITHMS: dict[str, Callable] = {
    'Metoda Alpinistului': solve_queens_hill_climbing,
    'Metoda Backtracking': regine_backtracking,
    'Metoda Alg. Genetici': solve_queens_genetic,
    'Metoda Sim. Annealing': solve_queens_simulated_annealing,
}


def show_n_regine_plot() -> None:
    table_sizes = [f"{n}x{n}" for n in TABLE_SIZES]
    test_cases = [generate_board(size) for size in TABLE_SIZES]

    for algorithm_name in ALGORITHMS:
        algorithm_times = []
        for board in test_cases:
            start_time = time.time()
            _ = ALGORITHMS[algorithm_name](board)
            end_time = time.time()

            algorithm_times.append(end_time - start_time)

        plt.plot(table_sizes, algorithm_times, label=algorithm_name)

    plt.xlabel("Marime tabla")
    plt.ylabel("Timp de executie [secunde]")
    plt.title("Comparare timpi executie algoritmit N regine")
    plt.legend()
    plt.grid()
    plt.show()
    input("Press Enter to continue...")
