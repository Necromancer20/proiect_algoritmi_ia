import sys

def solve_tsp_nearest_neighbor(graph, start=0):
    n = len(graph)
    visited = [False] * n
    path = [start]
    total_cost = 0

    curr_city = start
    visited[start] = True

    while len(path) < n:
        min_cost = sys.maxsize
        next_city = None
        for neighbor in range(n):
            if not visited[neighbor] and graph[curr_city][neighbor] < min_cost:
                min_cost = graph[curr_city][neighbor]
                next_city = neighbor
        
        if next_city is not None:
            path.append(next_city)
            visited[next_city] = True
            total_cost += min_cost
            curr_city = next_city
        else:
            # If there are no unvisited neighbors, return to the start
            total_cost += graph[curr_city][start]
            path.append(start)
            break

    return total_cost, path
