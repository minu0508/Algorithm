def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1), 1):
        Save_List = []
        for j in range(0, len(arr1[i]), 1):
            Save_List.append(arr1[i][j] + arr2[i][j])
        answer.append(Save_List)
    return answer