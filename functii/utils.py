import random


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



