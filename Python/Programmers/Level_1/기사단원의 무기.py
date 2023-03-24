def solution(number, limit, power):
    answer = 0
    count = [0] * (number + 1)

    for i in range(1, number+1, 1):
        for j in range(i, number + 1, i):
            count[j] += 1

    for k in range(0, len(count), 1):
        if (count[k] > limit):
            answer += power
        else:
            answer += count[k]
    return answer