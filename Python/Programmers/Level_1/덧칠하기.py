def solution(n, m, section):
    answer =  0
    savePaint = 0
    for i in range(len(section)):
        if  savePaint < section[i]:
            answer += 1
            savePaint = section[i] + m - 1
    return answer