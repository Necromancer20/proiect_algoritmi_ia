import time, random

from algorithms.comis_voiajor_backtracking_recursiv import solve_tsp_backtracking
from functions.utils import generate_random_distances


def show_tsp_recursive_backtracking_option():
    n_cities = 5  # Number of cities
    distances = generate_random_distances(n_cities)

    start_city = random.randint(0, n_cities-1)

    start_time = time.time()
    min_cost, optimal_path = solve_tsp_backtracking(distances, start_city)
    end_time = time.time()
    print(f"Solution found in {end_time - start_time:.2f} seconds.")

    if min_cost is not None:
        print(f"Initial distances:\n")
        for row in distances:
            print(' '.join(map(str, row)))
        print(f"Minimum cost for TSP starting from city {start_city}: {min_cost}")
        print("Optimal Path:", optimal_path)
    else:
        print("No solution found.")
