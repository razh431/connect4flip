import numpy as np
ROW_COUNT = 6
COLUMN_COUNT = 7


board = np.array([[1, 2, 2, 1, 1, 0, 0],
                  [0, 1, 1, 2, 0, 0, 0],
                  [0, 0, 3, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def gravity(board):
    for col in range(COLUMN_COUNT):
        row = get_next_open_row(board, col)
        zeroes_cols = np.zeros(ROW_COUNT - row)

        flattened = board[:, col].flatten()
        new_col = np.append(zeroes_cols, flattened)[:6]
        board[:, col] = new_col
    return board


print(gravity(board))
