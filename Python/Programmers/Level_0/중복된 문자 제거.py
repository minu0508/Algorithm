def solution(my_string):
    answer = ''
    my_string = list(my_string)
    my_string = list(dict.fromkeys(my_string))
    
    for i in range(0, len(my_string), 1):
        answer += my_string[i]
        
    return answer