def solution(array):
    answer = 0
    for i in range(0, len(array), 1):
        array[i] = array[i] * 2
    answer = array
    return answer