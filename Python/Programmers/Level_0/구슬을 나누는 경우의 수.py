def solution(balls, share):
    answer = 0
    n = (balls - share)
    m = share
    Save_n = 1
    Save_m = 1
    Save_balls = 1

    for i in range(n, 0, -1):
        Save_n *= i

    for j in range(m, 0, -1):
        Save_m *= j
    
    for k in range(balls, 0, -1):
        Save_balls *= k

    answer = Save_balls // (Save_n * Save_m)
    return answer