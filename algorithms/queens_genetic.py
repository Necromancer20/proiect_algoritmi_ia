import random
import utils.utils as utils

POPULATION_SIZE = 50
MUTATION_RATE = 0.1
MAX_GENERATIONS = 1000


def solve_queens_genetic(board):
    n = len(board)
    population = [(utils.generate_random_board(n), 0) for _ in range(POPULATION_SIZE)]
    for generation in range(MAX_GENERATIONS):
        population = [(board_state, utils.count_attacks(board_state)) for board_state, _ in population]
        best_board_state = max(population, key=lambda x: x[1])[0]
        if utils.count_attacks(best_board_state) == 0:
            print("Solution found in generation", generation)
            return best_board_state  # Return the solution when found
        new_population = []
        new_population.append(max(population, key=lambda x: x[1]))
        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population, n)
            parent2 = tournament_selection(population, n)
            child = crossover(parent1[0], parent2[0], n)
            if random.random() < MUTATION_RATE:
                child = mutate(child, n)
            new_population.append((child, 0))
        population = new_population
    print("No solution found after", MAX_GENERATIONS, "generations.")
    return None  # Return None if no solution is found


def tournament_selection(population, n):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda x: x[1])


def crossover(parent1, parent2, n):
    crossover_point = random.randint(1, n - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate(board_state, n):
    pos1, pos2 = random.sample(range(n), 2)
    board_state[pos1], board_state[pos2] = board_state[pos2], board_state[pos1]
    return board_state


# Ensure that the generate_random_board function generates boards with one queen per row and column
def generate_random_board(n):
    board = [0] * n
    for i in range(n):
        board[i] = random.randint(0, n - 1)
    return board

# Now you can call solve_queens_genetic(board) with a valid board to solve the N-Queens problem using genetic algorithm.
