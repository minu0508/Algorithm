def solution(n):
    answer = 0
    Num = 1
    while(True):
        Save = Num * 6
        Num += 1
        if (Save % n == 0):
            answer = Save // 6
            break
    return answer