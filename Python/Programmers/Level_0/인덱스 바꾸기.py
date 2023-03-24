def solution(my_string, num1, num2):
    answer = ''
    my_string = list(str(my_string))
    
    A = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = A
    
    for i in range(0, len(my_string), 1):
        answer += my_string[i]
    return answer