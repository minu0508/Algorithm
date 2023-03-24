def solution(i, j, k):
    answer = 0
    K_str = str(k)
    for i in range(i, j+1, 1):
        Num_str = list(str(i))
        if (Num_str.count(K_str) > 0):
            answer += Num_str.count(K_str)
    return answer