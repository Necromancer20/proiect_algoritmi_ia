def comis_voiajor_recursive_backtracking(distances, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if len(visited) == len(distances):
        return sum(distances[path[i - 1]][path[i]] for i in range(len(path)))

    for next_city in range(len(distances)):
        if next_city not in visited:
            visited.add(next_city)
            path.append(next_city)

            result = comis_voiajor_recursive_backtracking(distances, visited.copy(), path)

            if result is not None:
                return result

            visited.remove(next_city)
            path.pop()

    return None
