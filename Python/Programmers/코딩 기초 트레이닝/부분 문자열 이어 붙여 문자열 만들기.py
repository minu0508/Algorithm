def solution(my_string):
    answer = []
    Save_str = ''
    for i in range(0, len(my_string), 1):
        answer.append(my_string[i:])
    answer.sort()
    return answer