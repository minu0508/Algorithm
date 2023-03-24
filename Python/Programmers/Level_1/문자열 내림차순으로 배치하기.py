def solution(s):
    answer = ''
    s = sorted(list(str(s)))
    s.reverse()
    for i in s:
        answer += i
    return answer