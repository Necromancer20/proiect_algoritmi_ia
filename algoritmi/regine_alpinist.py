import copy


def solve_regine_alpinist(board: list[list[int]]) -> list[list[int]]:
    return hill_climbing(board)


def count_violations(board):
    violations = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in range(len(board)):
                    if board[k][j] == 1 and i != k:
                        violations += 1
                    if board[i][k] == 1 and j != k:
                        violations += 1
                    if i + j == k + j and i != k:
                        violations += 1
                    if i - j == k - j and i != k:
                        violations += 1
    return violations


def move_queen(board, row, col, new_row, new_col):
    board[row][col] = 0
    board[new_row][new_col] = 1


def hill_climbing(board):
    best_board = copy.deepcopy(board)
    best_violations = count_violations(board)
    while True:
        improved = False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != 1:
                    continue

                for new_row in range(len(board)):
                    for new_col in range(len(board[new_row])):
                        if board[new_row][new_col] != 0:
                            continue

                        move_queen(board, row, col, new_row, new_col)
                        violations = count_violations(board)
                        if violations < best_violations:
                            best_violations = violations
                            best_board = copy.deepcopy(board)
                            improved = True
                        move_queen(board, new_row, new_col, row, col)

        if not improved:
            break
    return best_board
