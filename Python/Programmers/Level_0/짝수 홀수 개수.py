def solution(num_list):
    answer = []
    A = 0
    B = 0
    for i in range(0, len(num_list), 1):
        if (num_list[i] % 2 == 0):
            A += 1
        else:
            B += 1
            
    answer.append(A)
    answer.append(B)
    return answer