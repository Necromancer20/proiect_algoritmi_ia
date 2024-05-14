import numpy as np

def generate_random_distances(n_cities):
    distances = np.random.randint(1, 100, size=(n_cities, n_cities))
    np.fill_diagonal(distances, 0)
    return distances.tolist()
def nearest_neighbor(distances, start_city=0):
    visited = set([start_city])
    path = [start_city]

    while len(visited) < len(distances):
        current_city = path[-1]
        next_city = min((city for city in range(len(distances)) if city not in visited),
                        key=lambda city: distances[current_city][city], default=None)
        if next_city is None:
            break  # No unvisited cities left
        visited.add(next_city)
        path.append(next_city)

    return path