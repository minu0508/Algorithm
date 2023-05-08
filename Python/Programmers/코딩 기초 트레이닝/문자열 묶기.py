def solution(strArr):
    answer = 0
    strArr_len = []
    for i in strArr:
        strArr_len.append(len(i))
    len_set = list(set(strArr_len))
    
    len_ea = [strArr_len.count(i) for i in len_set] 
    return max(len_ea)