def solution(before, after):
    answer = 0
    before = sorted(list(str(before)))
    after = sorted(list(str(after)))
    
    for i in range(0, len(before), 1):
        if (before[i] != after[i]):
            answer = 0
            break
        else:
            answer = 1
    return answer