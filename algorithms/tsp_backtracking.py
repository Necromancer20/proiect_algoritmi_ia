import sys

def solve_tsp_backtracking(graph, start=0):
    n = len(graph)
    visited = [False] * n
    path = [start]
    min_cost = [sys.maxsize]
    min_path = []

    visited[start] = True

    def backtrack(curr, cost):
        if len(path) == n:
            # If all cities are visited, return to the start
            cost += graph[curr][start]
            if cost < min_cost[0]:
                min_cost[0] = cost
                min_path[:] = path[:]  # Update the minimum path
            return

        for next_city in range(n):
            if not visited[next_city]:
                # Visit the next unvisited city
                visited[next_city] = True
                path.append(next_city)
                backtrack(next_city, cost + graph[curr][next_city])
                # Backtrack
                visited[next_city] = False
                path.pop()

    backtrack(start, 0)
    min_path.append(start)  # Add the start city to complete the cycle
    return min_cost[0], min_path