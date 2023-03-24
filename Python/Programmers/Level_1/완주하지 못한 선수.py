import collections as col

def solution(participant, completion):
    answer = ''
    dic = col.Counter(participant)
    for i in completion:
        if i in dic and dic.get(i) >= 1:
            dic[i] = dic.get(i) - 1

    for j, k in dic.items():
        if (k == 1):
            answer = j
    
    return answer