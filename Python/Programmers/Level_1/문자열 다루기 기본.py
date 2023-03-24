def solution(s):
    answer = 0
    s = list(str(s))
    Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if (len(s) == 4 or len(s) == 6):
        for i in range(0, len(s), 1):
            if (Numbers.count(s[i]) == 0):
                answer = False
                break
            elif (Numbers.count(s[i]) > 0):
                answer = True
    else:
        answer = False
    return answer