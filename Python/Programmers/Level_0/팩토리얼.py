def solution(n):
    answer = 0
    Num = 1
    Plus = 1
    
    while(True):
        if (n >= Num):
            Num *= Plus
            Plus += 1
            answer += 1
        elif (n < Num):
            answer -= 1
            break
    return answer