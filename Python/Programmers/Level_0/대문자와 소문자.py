def solution(my_string):
    answer = ''
    my_string = list(str(my_string))
    
    for i in my_string:
        A = i.isupper()
        if (A == False):
            i = i.upper()
            answer += i
        else:
            i = i.lower()
            answer += i
    return answer