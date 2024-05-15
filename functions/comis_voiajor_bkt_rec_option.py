import time

from algorithms.comis_voiajor_backtracking_recursiv import comis_voiajor_recursive_backtracking
from functions.utils import generate_random_distances


def show_tsp_recursive_backtracking_option():
    n_cities = 5  # Number of cities
    distances = generate_random_distances(n_cities)
    start_time = time.time()
    result = comis_voiajor_recursive_backtracking(distances)
    end_time = time.time()
    print(f"Solution found in {end_time - start_time:.2f} seconds.")

    if result is not None:
        print(f"Initial distances:\n")
        for row in distances:
            print(' '.join(map(str, row)))
        print(f"Solved path:\n")
        print(result)
    else:
        print("No solution found.")
