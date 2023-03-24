def solution(left, right):
    answer = 0
    for i in range(left, right+1, 1):
        Save_List = []
        for j in range(1, i+1, 1):
            if (i % j == 0):
                Save_List.append(j)
        if (len(Save_List) % 2 == 0):
            answer += i
        elif (len(Save_List) % 2 == 1):
            answer -= i
    return answer