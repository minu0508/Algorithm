def solution(s):
    answer = ''
    s = s.split(' ')
    for j in s:
        for i in range(0, len(j), 1):
            if (i % 2 == 0):
                answer += j[i].upper()
            else:
                answer += j[i].lower()
        answer += ' '
    answer = answer[:-1]
    return answer
