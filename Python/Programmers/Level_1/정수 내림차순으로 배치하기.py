def solution(n):
    n = sorted(list(str(n)))
    n.reverse()
    answer = ''
    
    for i in n:
        answer += i
        
    return int(answer)