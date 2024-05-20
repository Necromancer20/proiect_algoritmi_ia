import random

import numpy as np


def read_board(input_file_path: str) -> list[list[int]]:
    board = []

    with open(input_file_path, 'r') as file:
        for line in file:
            board.append(
                list(
                    map(int, list(line.strip()))
                )
            )

    return board


def print_board(board: list[list[int]]) -> None:
    for line in board:
        print(''.join(map(str, line)))


def generate_board(size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    possible_positions = [(i, j) for j in range(size) for i in range(size)]

    picked_pos = random.choices(possible_positions, k=size)

    for i, j in picked_pos:
        board[i][j] = 1

    print_board(board)
    return board


# Simulated Annealing
def add_attacks(board):
    attacks = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in range(i + 1, len(board)):
                    if board[k][j] == 1:
                        attacks += 1
                for k in range(len(board)):
                    if board[i][k] == 1 and j != k:
                        attacks += 1
                    if i + j == k + j and i != k:
                        attacks += 1
                    if i - j == k - j and i != k:
                        attacks += 1
    return attacks


def count_attacks(board):
    attacks = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in range(i + 1, len(board)):
                    if board[k][j] == 1:
                        attacks += 1
                for k in range(len(board)):
                    if board[i][k] == 1 and j != k:
                        attacks += 1
                    if i + j == k + j and i != k:
                        attacks += 1
                    if i - j == k - j and i != k:
                        attacks += 1
    return attacks


# Genetic algorithm


def generate_board_state(n):
    board_state = [[0 for _ in range(n)] for _ in range(n)]  # Initialize a 2D board
    for i in range(n):
        for j in range(n):
            board_state[i][j] = random.randint(0, n - 1)  # Randomly assign values to the board
    return board_state


def calculate_fitness(board_state, n):
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board_state[i] == board_state[j] or abs(board_state[i] - board_state[j]) == j - i:
                conflicts += 1
    return n * (n - 1) / 2 - conflicts  # Max fitness = n*(n-1)/2 (no conflicts)


def tournament_selection(population, n):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x[1])


# comis voiajor
def read_graph(input_file_path: str) -> list[list[int]]:
    graph = []

    with open(input_file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            graph.append(row)

    return graph


def print_path(path):
    for index in path:
        print(index, end=' ')
    print()


def generate_random_distances(n_cities):
    # Generate a square matrix of random distances
    distances = [[0] * n_cities for _ in range(n_cities)]

    for i in range(n_cities):
        for j in range(i+1, n_cities):
            distances[i][j] = distances[j][i] = random.randint(1, 100)

    #np.fill_diagonal(distances, 0)  # Diagonal elements represent the distance from a city to itself, which is 0
    return distances#.tolist()
