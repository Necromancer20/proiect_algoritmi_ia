import numpy as np
import matplotlib.pyplot as plt
import time

def generate_random_distances(n_cities):
    distances = np.random.randint(1, 100, size=(n_cities, n_cities))
    np.fill_diagonal(distances, 0)
    return distances.tolist()

def tsp_recursive_backtracking(distances, current_city=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if len(visited) == len(distances):
        return sum(distances[path[i-1]][path[i]] for i in range(len(path)))

    for next_city in range(len(distances)):
        if next_city not in visited:
            visited.add(next_city)
            path.append(next_city)

            result = tsp_recursive_backtracking(distances, next_city, visited.copy(), path)

            if result is not None:
                return result

            visited.remove(next_city)
            path.pop()

    return None

def nearest_neighbor(distances, start_city=0):
    visited = set([start_city])
    path = [start_city]

    while len(visited) < len(distances):
        current_city = path[-1]
        next_city = min((city for city in range(len(distances)) if city not in visited),
                        key=lambda city: distances[current_city][city], default=None)
        if next_city is None:
            break
        visited.add(next_city)
        path.append(next_city)

    return path

def calculate_total_distance(path, distances):
    return sum(distances[path[i-1]][path[i]] for i in range(len(path)))

def plot_tsp_results(n_cities, num_trials=10):
    distances = generate_random_distances(n_cities)
    recursive_backtracking_distances = []
    nearest_neighbor_distances = []

    for _ in range(num_trials):
        start_time = time.time()
        result = tsp_recursive_backtracking(distances)
        end_time = time.time()
        recursive_backtracking_distances.append(calculate_total_distance(result, distances))

        start_time = time.time()
        result = nearest_neighbor(distances)
        end_time = time.time()
        nearest_neighbor_distances.append(calculate_total_distance(result, distances))

    plt.figure(figsize=(10, 6))
    plt.bar(['Recursive Backtracking', 'Nearest Neighbor'], [np.mean(recursive_backtracking_distances), np.mean(nearest_neighbor_distances)])
    plt.ylabel('Average Total Distance')
    plt.title(f'Average Total Distance for {num_trials} Trials')
    plt.show()

def plot_tsp_results_option():
    n_cities = int(input("Enter the number of cities: "))
    plot_tsp_results(n_cities, num_trials=10)