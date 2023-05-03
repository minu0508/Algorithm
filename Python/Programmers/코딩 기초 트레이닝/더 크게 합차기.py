def solution(a, b):
    case_1 = int(str(a) + str(b))
    case_2 = int(str(b) + str(a))
    
    if (case_1 > case_2):
        return case_1
    else:
        return case_2