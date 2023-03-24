def solution(arr):
    answer = []
    Num = 0
    Save = arr[0]
    answer.append(Save)
    for i in range(1, len(arr), 1):
        Save = arr[i]
        if (answer[Num] != arr[i]):
            answer.append(Save)
            Num += 1
    return answer