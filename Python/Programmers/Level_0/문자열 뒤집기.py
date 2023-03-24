def solution(my_string):
    Str = list(map(str, my_string))
    Str.reverse()
    answer = ''
    
    for i in Str:
        answer += i
    return answer