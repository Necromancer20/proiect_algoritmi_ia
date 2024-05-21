import time,random

from algorithms.comis_voiajor_apropiat_vecin import solve_tsp_nearest_neighbor
from functions.utils import generate_random_distances


def show_tsp_nearest_neighbor_option():
    n_cities = 5  # Number of cities
    distances = generate_random_distances(n_cities)
    start_city = random.randint(0, n_cities-1)

    start_time = time.time()
    min_cost, optimal_path = solve_tsp_nearest_neighbor(distances, start_city)
    end_time = time.time()
    print(f"Solution found in {end_time - start_time:.2f} seconds.")

    if optimal_path is not None:
        print(f"Initial distances:\n")
        for row in distances:
            print(' '.join(map(str, row)))
        print(f"Solved path:\n")
        print(f"Minimum cost for TSP using nearest neighbor starting from city {start_city}: {min_cost}")
        print("Optimal Path:", optimal_path)
    else:
        print("No solution found.")
