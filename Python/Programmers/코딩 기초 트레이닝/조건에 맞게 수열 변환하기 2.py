def solution(arr):
    for i in range(len(arr)):
        step = 0
        for j in range(len(arr)):
            if (arr[j] >= 50 and arr[j] % 2 == 0):
                arr[j] = arr[j] // 2
            elif (arr[j] < 50 and arr[j] % 2 != 0):
                arr[j] = arr[j] * 2 + 1
            else:
                step += 1
                
            if(step == len(arr)):
                return i