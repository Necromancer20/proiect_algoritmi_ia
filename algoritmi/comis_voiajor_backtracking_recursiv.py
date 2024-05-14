import numpy as np

def generate_random_distances(n_cities):
    # Generate a square matrix of random distances
    distances = np.random.randint(1, 100, size=(n_cities, n_cities))
    np.fill_diagonal(distances, 0)  # Diagonal elements represent the distance from a city to itself, which is 0
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
