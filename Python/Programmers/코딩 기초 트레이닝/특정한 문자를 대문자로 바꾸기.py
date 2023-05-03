def solution(my_string, alp):
    alp_up = alp.upper()
    
    my_string = my_string.replace(alp, alp_up)
    return my_string