import copy, random, math

def solve_queens_simulated_annealing(board):
    # Step 1: Apply simulated annealing
    return simulated_annealing(board)

def count_attacks(board):
    """
    Counts the number of attacks (conflicts) on the board.
    
    Args:
        board: A 2D list representing the chessboard with queens' positions.
        
    Returns:
        The number of conflicts (attacks) on the board.
    """
    n = len(board)
    attacks = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # Check row and column conflicts
                for k in range(n):
                    if k != i and board[k][j] == 1:
                        attacks += 1
                    if k != j and board[i][k] == 1:
                        attacks += 1
                
                # Check diagonal conflicts
                for k in range(1, n):
                    # Check major diagonal (i + k, j + k) and (i - k, j - k)
                    if i + k < n and j + k < n and board[i + k][j + k] == 1:
                        attacks += 1
                    if i - k >= 0 and j - k >= 0 and board[i - k][j - k] == 1:
                        attacks += 1
                    # Check minor diagonal (i + k, j - k) and (i - k, j + k)
                    if i + k < n and j - k >= 0 and board[i + k][j - k] == 1:
                        attacks += 1
                    if i - k >= 0 and j + k < n and board[i - k][j + k] == 1:
                        attacks += 1

    # Each attack is counted twice, so divide by 2
    return attacks // 2

def simulated_annealing(board):
    current_solution = copy.deepcopy(board)
    current_cost = count_attacks(current_solution)
    T = 10000  # Initial temperature
    alpha = 0.95  # Cooling rate
    min_temp = 0.0001  # Minimum temperature

    n = len(board)

    while T > min_temp:
        # Generate a new solution by moving one queen to a new column in its row
        new_solution = copy.deepcopy(current_solution)
        row = random.randint(0, n - 1)
        current_col = next((col for col in range(n) if current_solution[row][col] == 1), None)

        if current_col is not None:
            new_col = random.randint(0, n - 1)
            while new_col == current_col:
                new_col = random.randint(0, n - 1)

            new_solution[row][current_col] = 0
            new_solution[row][new_col] = 1
            new_cost = count_attacks(new_solution)

            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
                current_solution = new_solution
                current_cost = new_cost

        T *= alpha

    return current_solution
