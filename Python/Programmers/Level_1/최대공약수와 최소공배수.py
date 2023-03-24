def solution(n, m):
    answer = []
    
    for i in range(min(n, m)+1, 0, -1):
        if (n % i == 0 and m % i == 0):
            answer.append(i)
            break 
    
    if (m % n == 0):
        answer.append(m)
    elif (m % n != 0):
        for i in range(1, n+1, 1):
            if (m*i % n == 0):
                answer.append(m*i)
                break
    return answer