def solution(my_string):
    answer = ''
    Collect = []
    my_string = list(str(my_string))
    
    for i in my_string:
        A = i.isupper()
        Save = i
        if (A == False):
            Collect.append(i)
        else:
            i = i.lower()
            Collect.append(i)

    Collect = sorted(Collect)
    for j in range(0, len(Collect), 1):
        answer += Collect[j]
        
    return answer