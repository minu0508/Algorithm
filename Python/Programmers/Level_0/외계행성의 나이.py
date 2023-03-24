def solution(age):
    answer = ''
    Alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age = list(str(age))
    for i in range(len(age)):
        answer += Alpha[int(age[i])]
    
    return answer