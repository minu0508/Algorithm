def solution(board, moves):
    answer = 0
    Num = 0
    length = len(board)
    Save_Number = 0
    Save = []
    
    for i in range(0, len(moves), 1):
        Num = moves[i] - 1
        for j in range(0, length, 1):
            Save_Number = board[j][Num]
            if (Save_Number != 0):
                Save.append(Save_Number)
                board[j][Num] = 0
                break           
    
        if (len(Save) >= 2):
            if (Save[-1] == Save[-2]):
                Save.pop(-1)
                Save.pop(-1)
                answer += 2
    return answer