def solution(s1, s2):
    answer = 0
    for i in range(0, len(s1), 1):
        answer += s2.count(s1[i])
    return answer