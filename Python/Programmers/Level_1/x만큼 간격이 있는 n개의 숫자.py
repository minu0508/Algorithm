def solution(x, n):
    answer = []
    num = x
    for i in range(0, n, 1):
        answer.append(num)
        num += x
    return answer