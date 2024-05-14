import random

from functii.utils import generate_board_state, POPULATION_SIZE, MAX_GENERATIONS, calculate_fitness, \
    tournament_selection, crossover, MUTATION_RATE, mutate, count_attacks, generate_board


def regine_genetic_algorithm(n):
    population = [(generate_board(n), 0) for _ in range(POPULATION_SIZE)]
    for generation in range(MAX_GENERATIONS):
        population = [(board_state, count_attacks(board_state)) for board_state, _ in population]
        best_board_state = max(population, key=lambda x: x[1])[0]
        if count_attacks(best_board_state) == 0:
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