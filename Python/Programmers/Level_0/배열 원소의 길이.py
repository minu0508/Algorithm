def solution(strlist):
    answer = []
    for i in range(0, len(strlist), 1):
        answer.append(len(list(map(str, strlist[i]))))
    return answer