def solution(n):
    answer = 0

    for i in range(4, n+1, 1):
        n_list = []
        for j in range(1, i+1, 1):
            if (i % j == 0):
                n_list.append(j)
        if (len(n_list) >= 3):
            answer += 1 
    return answer