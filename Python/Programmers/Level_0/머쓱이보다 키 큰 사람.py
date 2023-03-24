def solution(array, height):
    answer = 0
    for i in range(0, len(array), 1):
        if (height < array[i]):
            answer += 1
    return answer