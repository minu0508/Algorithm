def solution(arr, queries):
    answer = []
    for i in queries:
        save_arr = arr[i[0] : i[1] + 1]
        save_arr.sort()
        for j in range(len(save_arr)):
            if (save_arr[j] > i[2]):
                answer.append(save_arr[j])
                break
        else:
            answer.append(-1)
    return answer