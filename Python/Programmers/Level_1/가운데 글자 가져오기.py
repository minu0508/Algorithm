def solution(s):
    answer = ''
    Save = []
    s = list(str(s))
    
    if (len(s) % 2 == 0):
        Num = (len(s)//2) - 1
        for _ in range(0, 2, 1):
            Save.append(s[Num])
            Num += 1
        for i in range(0, len(Save), 1):
            answer += Save[i]
    else:
        Num = len(s)//2
        answer += s[Num]
    return answer