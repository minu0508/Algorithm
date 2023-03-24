def solution(emergency):
    answer = []
    Sort_E = sorted(emergency)
    Sort_E.reverse()

    for i in range(0, len(emergency), 1):
        answer.append(Sort_E.index(emergency[i]) + 1)
    return answer