def solution(arr, delete_list):
    answer = []
    for i in range(len(arr)):
        if (delete_list.count(arr[i]) == 0):
            answer.append(arr[i])
    return answer