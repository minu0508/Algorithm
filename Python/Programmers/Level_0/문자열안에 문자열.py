def solution(str1, str2):
    answer = 0
    Count = 0
    Count = str1.count(str2)
    if (Count >= 1):
        answer = 1
    else:
        answer = 2
    return answer