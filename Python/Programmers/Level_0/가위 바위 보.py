def solution(rsp):
    answer = ''
    rsp = list(rsp)
    
    for i in range(0, len(rsp), 1):
        if (rsp[i] == '2'):
            answer += '0'
        elif (rsp[i] == '0'):
            answer += '5'
        else:
            answer += '2'
    
    return answer