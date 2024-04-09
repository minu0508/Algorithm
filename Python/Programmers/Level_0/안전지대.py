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

#24-04-09
import numpy as np

def solution(board):
    newBoard, answerBoard = [], []
    
    for i in board:
        i = [0] + i + [0]
        newBoard.append(i)
    newBoard = ([[0] * len(newBoard[0])]) + newBoard + ([[0] * len(newBoard[0])])
    newBoard = np.array(newBoard)
    
    x, y = np.where(newBoard==1)
    for x, y in zip(x, y):
        newBoard[x-1:x+2, y-1:y+2] = 1
    
    for i in range(1, len(newBoard)-1, 1):
        answerBoard.append(newBoard[i][1:len(newBoard)-1])
    answerBoard = np.array(answerBoard)
    
    return len(answerBoard[answerBoard==0])
