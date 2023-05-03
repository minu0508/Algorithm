def solution(my_string):
    my_string += ' '
    answer = []
    Save_str = ''
    for i in my_string:
        if (i != " "):
            Save_str += i
        else:
            answer.append(Save_str)
            Save_str = ''
    for j in range(0, answer.count(''), 1):
        answer.remove('')
    return answer