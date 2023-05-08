def solution(arr):
    answer = []
    front, back = 0, 0
    if (arr.count(2) == 1):
        return [2]
    elif (arr.count(2) == 0):
        return [-1]
    else:
        for i in range(0, len(arr), 1):
            if (arr[i] == 2):
                front = i
                break
        for j in range(len(arr)-1, -1, -1):
            if (arr[j] == 2):
                back = j
                break
        return arr[front : back + 1]