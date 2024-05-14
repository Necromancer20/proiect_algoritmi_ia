import time
from typing import Callable

import matplotlib.pyplot as plt

from algoritmi.comis_voiajor_apropiat_vecin import comis_voiajor_nearest_neighbor
from algoritmi.comis_voiajor_backtracking_recursiv import comis_voiajor_recursive_backtracking
from functii.utils import generate_random_distances

ROAD_SIZES = (30, 60, 100, 150, 200, 500)
ALGORITHMS: dict[str, Callable] = {
    'Metoda alg. celui mai apropiat vecin': comis_voiajor_recursive_backtracking,
    'Metoda backtracking recursiv': comis_voiajor_nearest_neighbor,
}


def show_comis_voiajor_regine_plot() -> None:
    test_cases = [generate_random_distances(size) for size in ROAD_SIZES]

    for algorithm_name in ALGORITHMS:
        algorithm_times = []
        for test_case in test_cases:
            start_time = time.time()
            _ = ALGORITHMS[algorithm_name](test_case)
            end_time = time.time()

            algorithm_times.append(end_time - start_time)

        plt.plot(ROAD_SIZES, algorithm_times, label=algorithm_name)

    plt.xlabel("Distanta")
    plt.ylabel("Timp de executie [secunde]")
    plt.title("Comparare timpi executie algoritmit Comis Voiajor")
    plt.legend()
    plt.grid()
    plt.show()
    input("Press Enter to continue...")
