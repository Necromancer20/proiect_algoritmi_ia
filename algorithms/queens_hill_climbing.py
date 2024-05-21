
import copy
def count_violations(board: list[list[int]]) -> int:
    """
    Counts the number of violations (conflicts) on the board.
    
    Args:
        board: A 2D list representing the chessboard with queens' positions.
        
    Returns:
        The number of conflicts (violations) on the board.
    """
    n = len(board)
    violations = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # Check column conflicts
                for k in range(n):
                    if k != i and board[k][j] == 1:
                        violations += 1
                
                # Check row conflicts
                for k in range(n):
                    if k != j and board[i][k] == 1:
                        violations += 1
                
                # Check diagonal conflicts
                for k in range(1, n):
                    # Check major diagonal (i + k, j + k) and (i - k, j - k)
                    if i + k < n and j + k < n and board[i + k][j + k] == 1:
                        violations += 1
                    if i - k >= 0 and j - k >= 0 and board[i - k][j - k] == 1:
                        violations += 1
                    # Check minor diagonal (i + k, j - k) and (i - k, j + k)
                    if i + k < n and j - k >= 0 and board[i + k][j - k] == 1:
                        violations += 1
                    if i - k >= 0 and j + k < n and board[i - k][j + k] == 1:
                        violations += 1

    return violations

def move_queen(board: list[list[int]], row: int, col: int, new_row: int, new_col: int) -> None:
    """
    Moves a queen from one position to another.
    
    Args:
        board: A 2D list representing the chessboard.
        row: The current row position of the queen.
        col: The current column position of the queen.
        new_row: The new row position of the queen.
        new_col: The new column position of the queen.
    """
    board[row][col] = 0
    board[new_row][new_col] = 1

def hill_climbing(board: list[list[int]]) -> list[list[int]]:
    """
    Solves the N-Queens problem using the hill climbing algorithm.
    
    Args:
        board: A 2D list representing the chessboard with queens' positions.
        
    Returns:
        A 2D list representing the chessboard with a (local) optimal solution.
    """
    best_board = copy.deepcopy(board)
    best_violations = count_violations(board)
    
    while True:
        improved = False
        
        # Iterate over each cell to find the queen
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != 1:
                    continue
                
                # Try moving the queen to every other cell in the same column
                for new_row in range(len(board)):
                    if new_row == row:
                        continue
                    if board[new_row][col] == 0:
                        # Move the queen to a new position and check for violations
                        move_queen(board, row, col, new_row, col)
                        violations = count_violations(board)
                        
                        # If this move reduces violations, keep it as the best move
                        if violations < best_violations:
                            best_violations = violations
                            best_board = copy.deepcopy(board)
                            improved = True
                        
                        # Move the queen back to the original position
                        move_queen(board, new_row, col, row, col)
        
        # If no improvement, break the loop
        if not improved:
            break
    
    return best_board


def solve_queens_hill_climbing(board: list[list[int]]) -> list[list[int]]:
    """
    Wrapper function to solve the N-Queens problem using the hill climbing algorithm.
    
    Args:
        board: A 2D list representing the initial chessboard configuration.
        
    Returns:
        A 2D list representing the chessboard with a (local) optimal solution.
    """
    return hill_climbing(board)
