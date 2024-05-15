def comis_voiajor_nearest_neighbor(distances, start_city=0):
    visited = {start_city}
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
