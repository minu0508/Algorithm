def solution(keyinput, board):
    answer = [0, 0]

    for i in range(len(keyinput)):
        if (keyinput[i] == "right"):
            answer[0] += 1
            if (abs(answer[0]) > abs(board[0] // 2)):
                answer[0] -= 1

        elif (keyinput[i] == "left"):
            answer[0] -= 1
            if (-(abs(answer[0])) < -(abs(board[0] // 2))):
                answer[0] += 1

        elif (keyinput[i] == "up"):
            answer[1] += 1
            if (abs(answer[1]) > abs(board[1] // 2)):
                answer[1] -= 1

        elif (keyinput[i] == "down"):
            answer[1] -= 1
            if (-(abs(answer[1])) < -(abs(board[1] // 2))):
                answer[1] += 1


    return answer