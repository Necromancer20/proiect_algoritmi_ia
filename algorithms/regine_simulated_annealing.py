import copy
import random
import math

from utils.utils import count_attacks


def regine_simulated_annealing(board):
    current_solution = board
    current_cost = count_attacks(current_solution)
    T = 10000  # Initial temperature
    alpha = 0.95  # Cooling rate
    min_temp = 0.0001  # Minimum temperature
    iterations = 0

    while T > min_temp:
        iterations += 1
        i, j = random.randint(0, len(board)-1), random.randint(0, len(board)-1)
        if current_solution[i][j] == 0:
            new_solution = copy.deepcopy(current_solution)
            new_solution[i][j] = 1
            new_cost = count_attacks(new_solution)

            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
                current_solution = new_solution
                current_cost = new_cost

        T *= alpha

    return current_solution