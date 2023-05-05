def solution(arr, queries):
    for i in queries:
        save_int = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = save_int
    return arr