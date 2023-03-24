def solution(s):
    answer = ''
    s = list(str(s))
    Save = []
    
    for i in s:
        if (s.count(i) == 1):
            Save.append(i)
            
    Save = sorted(Save)
    
    for j in Save:
        answer += j
    return answer