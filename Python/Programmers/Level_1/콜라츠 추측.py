def solution(num):
    if (num == 1):
        answer = 0
    else:
        answer = 0
        while (True):
            if (num != 1):
                if (num % 2 == 0):
                    num = num // 2
                    answer += 1
                elif (num % 2 == 1):
                    num = num * 3 + 1
                    answer += 1
            elif (num == 1):
                break        
            
            if (answer >= 500):
                answer = -1
                break
        
            
    return answer