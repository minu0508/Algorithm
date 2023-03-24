def solution(n):
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1

    if (n < 2):
        return n
    
    for i in range(2, n+1):
        d[i] = d[i - 1] + d[i - 2]
    
    return d[i] % 1234567