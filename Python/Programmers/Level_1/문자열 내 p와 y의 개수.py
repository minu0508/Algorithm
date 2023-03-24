def solution(s):
    s = list(map(str, s))
    
    Y = 0
    P = 0
    
    for i in s:
        if (i == 'p' or i == 'P'):
            Y += 1
        elif (i == 'y' or i == 'Y'):
            P += 1
    if (Y == P):
        return True
    else:
        return False