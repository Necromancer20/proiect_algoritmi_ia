import time
from typing import Callable

import matplotlib.pyplot as plt

from algoritmi.regine_alpinist import solve_regine_alpinist
from algoritmi.regine_backtracking import regine_backtracking
from algoritmi.regine_genetic_algorithm import regine_genetic_algorithm
from algoritmi.regine_simulated_annealing import regine_simulated_annealing
from functii.utils import generate_board

TABLE_SIZES = (3, 5, 10, 12, 13, 15, 20)
ALGORITHMS: dict[str, Callable] = {
    'Metoda Alpinistului': solve_regine_alpinist,
    'Metoda Backtracking': regine_backtracking,
    'Metoda Alg. Genetici': regine_genetic_algorithm,
    'Metoda Sim. Annealing': regine_simulated_annealing,
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
