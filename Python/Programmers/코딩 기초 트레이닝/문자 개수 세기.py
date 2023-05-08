import string

def solution(my_string):
    idx_alpha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    All_alpha = list(string.ascii_letters)
    All_alpha.sort()
    
    for i in my_string:
        idx_alpha[All_alpha.index(i)] += 1
    
    return idx_alpha