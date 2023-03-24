import numpy as np

def solution(board):
    answer = 0
    board = np.array(board)
    x, y = np.where(board == 1)

    for i, j in zip(x, y):
        if (j == 0):
            board[i-1:i+2, j:j+2] = 1
        else:
            board[i-1:i+2, j-1:j+2] = 1

    answer = len(board[board==0])
    
    return answer