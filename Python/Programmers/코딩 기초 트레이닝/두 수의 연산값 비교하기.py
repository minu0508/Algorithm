def solution(a, b):
    ab_str = str(a) + str(b)
    ab = 2 * a * b
    
    if (int(ab_str) >= ab):
        return int(ab_str)
    else:
        return ab