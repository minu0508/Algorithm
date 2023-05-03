def solution(n):
    result = []
    for i in range(n):
        answer = []
        for j in range(n):
            answer.append(0)
        answer[i] = 1
        result.append(answer)
    return result