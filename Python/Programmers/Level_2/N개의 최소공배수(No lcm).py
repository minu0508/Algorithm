def solution(arr):
    answer = 0
    arr.sort()
    arr_Max = max(arr)
    num = 1
    check_Num = 0
    while(True):
        Save = arr_Max * num
        for i in range(0, len(arr) - 1, 1):
            if (Save % arr[i] != 0):
                check_Num = 1
                num += 1
                break
            else:
                check_Num = 0
        if (check_Num == 0):
            break
    return answer