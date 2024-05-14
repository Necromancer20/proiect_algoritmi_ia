import time

from algoritmi.comis_voiajor_apropiat_vecin import generate_random_distances, nearest_neighbor


def show_tsp_nearest_neighbor_option():
    n_cities = 5  # Number of cities
    distances = generate_random_distances(n_cities)
    start_time = time.time()
    result = nearest_neighbor(distances)
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

# Example usage
if __name__ == "__main__":
    show_tsp_nearest_neighbor_option()
