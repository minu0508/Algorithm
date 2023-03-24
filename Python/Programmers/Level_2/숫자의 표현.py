def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        start = i
        save = start
        while (True):
            if (start == n):
                answer += 1
                break
            elif (start > n):
                break
            save += 1
            start += save

    return answer