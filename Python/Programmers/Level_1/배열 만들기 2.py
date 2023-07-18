def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if (i == 0):
            pass
        else:
            for j in str(i):
                if j != '5' and j != '0':
                    break
            else:
                answer.append(i)

    if (len(answer) == 0):
        return [-1]
    else:
        return answer