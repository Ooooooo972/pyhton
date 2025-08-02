import numpy as np
import random
from time import sleep

def create_board():
    return np.zeros((3, 3), dtype=int)

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def random_place(board, player):
    loc = random.choice(possibilities(board))
    board[loc] = player
    return board

def row_win(board, player):
    return any(all(cell == player for cell in row) for row in board)

def col_win(board, player):
    return any(all(row[i] == player for row in board) for i in range(3))

def diag_win(board, player):
    return all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def evaluate(board):
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    return -1 if np.all(board != 0) else 0

def play_game():
    board, winner, move = create_board(), 0, 1
    print(board)
    sleep(1)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"\nBoard after move {move}:\n{board}")
            sleep(1)
            move += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner

# Run the game
print(f"\nWinner is: {play_game()}")