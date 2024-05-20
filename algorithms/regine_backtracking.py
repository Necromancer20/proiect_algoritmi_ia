def solve_n_queens_backtracking(board: list[list[int]]) -> list[list[int]]:
    boardSize = len(board)

    solution = solve_n_queens_problem(boardSize, boardSize)

    return solution if solution else board


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed at board[row][col] in the given board.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n, num_queens):
    """
    Solve the N-Queens problem using backtracking.
    """
    # Base case: If all queens are placed
    if col >= num_queens:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1, n, num_queens):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column col then return false
    return False


def solve_n_queens_problem(size):
    """
    Function to solve N-Queens problem for any number of queens and any size of board.
    """
    # Create an empty board of size n x n
    board = [[0 for _ in range(size)] for _ in range(size)]

    # Solve the N-Queens problem using backtracking
    if not solve_n_queens(board, 0, size, size):
        return None

    return board
