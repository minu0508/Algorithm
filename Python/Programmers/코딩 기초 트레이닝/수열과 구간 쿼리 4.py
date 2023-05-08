def solution(arr, queries):
    for i in queries:
        for j in range(i[0], i[1]+1):
            if (j == 0):
                arr[0] += 1
            elif (j > 0 and j % i[2] == 0):
                arr[j] += 1
    return arr