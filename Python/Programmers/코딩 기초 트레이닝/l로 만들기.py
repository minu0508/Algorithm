import string

def solution(myString):
    alp_low = string.ascii_lowercase
    answer = ''
    
    for i in myString:
        if (alp_low.index(i) < alp_low.index("l")):
            answer += "l"
        else:
            answer += i
    return answer