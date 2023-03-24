def solution(lines):
    answer = []
    answer_list = []

    if (lines[0][1] == lines[1][0] and lines[1][1] == lines[2][0]):
        return 0
    else:
        for i in range(0, 3, 1):
            for j in range(lines[i][0], lines[i][1], 1):
                length = [j , j+1]      
                answer_list.append(length)
        if (answer_list == 0):
            return 0

        else:
            for k in answer_list:
                if (answer_list.count(k) >= 2):
                    if (answer.count(k) >= 1):
                        pass
                    else:
                        answer.append(k)
        answer = len(answer)
    return answer