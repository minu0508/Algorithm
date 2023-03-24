def solution(strings, n):
    answer = []
    Save_list = []
    
    for i in strings:
        i = list(i)
        i.insert(0, i[n])
        Save_list.append(i)
    Save_list.sort()
    
    for j in Save_list:
        Str = ''
        for k in range(1, len(j), 1):
            Str += j[k]
        answer.append(Str)
    return answer