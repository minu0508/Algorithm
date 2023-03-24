def solution(my_string, n):
    answer = ''
    my_string = list(str(my_string))
    for i in range(0, len(my_string), 1):
        answer += my_string[i]*n
    return answer