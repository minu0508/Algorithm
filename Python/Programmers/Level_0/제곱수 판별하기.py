def solution(n):
    answer = 0
    number = 1
    while(True):
        if (number*number == n):
            answer = 1
            break
            
        elif (number*number > n):
            answer = 2
            break
            
        number += 1
    return answer