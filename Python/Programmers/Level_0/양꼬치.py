def solution(n, k):
    answer = 0
    answer += 12000 * n
    if (n >= 10):
        Juice = n // 10
        answer = (12000 * n) + ((k - Juice) * 2000)
    else:
        answer = (12000 * n) + (k * 2000)
    return answer