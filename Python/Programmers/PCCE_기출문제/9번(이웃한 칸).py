def solution(board, h, w):
    answer = 0
    zero_list = ["0" for _ in range(len(board) + 2)]
    h += 1
    w += 1
    
    for i in range(len(board[0])):
        board[i].insert(0, "0")
        board[i].insert(len(board) + 1, "0")
    board.insert(0, zero_list)
    board.insert(len(board), zero_list)
        
    if (board[h-1][w] == board[h][w]):
        answer += 1
    if (board[h+1][w] == board[h][w]):
        answer += 1
        
    for width in range(w-1, w+2, 1):
        if (width == w):
            pass
        else:
            if (board[h][width] == board[h][w]):
                answer += 1
            
    return answer