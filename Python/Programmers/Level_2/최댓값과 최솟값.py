def solution(s):
    answer = ''
    s = list(map(int, s.split()))
    answer = str(min(s)) + " " + str(max(s))
    return answer

solution("-1 -2 -3 -4")