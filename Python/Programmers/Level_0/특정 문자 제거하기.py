def solution(my_string, letter):
    my_string = list(str(my_string))
    Count = my_string.count(letter)
    answer = ''
    
    for i in range(0, Count, 1):
        my_string.remove(letter)
    
    for j in range(0, len(my_string), 1):
        answer += my_string[j]    
    return answer