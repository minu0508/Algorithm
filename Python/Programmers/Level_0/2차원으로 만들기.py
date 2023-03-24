def solution(num_list, n):
    answer = []
    Save = []
    Num = 0
    while(True):
        if (len(Save) <= (n-1)):
            Save.append(num_list[Num])
            Num += 1
        elif (len(Save) == n):
            answer.append(Save)
            Save = []
            
        if (len(num_list)//n == len(answer)):
            break
    return answer