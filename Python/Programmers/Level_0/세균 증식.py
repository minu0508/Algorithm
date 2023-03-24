def solution(n, t):
    answer = n
    for i in range(0, t, 1):
        answer += answer
    return answer