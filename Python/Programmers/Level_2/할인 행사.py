import collections

def solution(want, number, discount):
    answer = 0
    wantDict = {want[i] : number[i] for i in range(len(want))}
    
    for j in range(len(discount)-9):
        if collections.Counter(discount[j:j+10]) == wantDict:
            answer += 1
            
    return answer