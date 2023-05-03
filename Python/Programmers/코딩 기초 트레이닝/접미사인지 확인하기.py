def solution(my_string, is_suffix):
    answer = 0
    Save_str = my_string[len(my_string) - len(is_suffix) : ]
    if (Save_str == is_suffix):
        answer = 1
    return answer