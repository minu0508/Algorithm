def solution(my_string):
    A = []
    answer = ''
    Alpha = ['a', 'e', 'i', 'o', 'u']
    my_string = list(str(my_string))
    
    for j in Alpha:
        for i in my_string:
            if (j == i):
                A.append(j)
                
    for k in range(0, len(A), 1):
        my_string.remove(A[k])

    for _ in range(0, len(my_string), 1):
        answer += my_string[_]

    return answer