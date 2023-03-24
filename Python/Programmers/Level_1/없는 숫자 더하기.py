def solution(numbers):
    answer = 0
    Not = []
    for i in range(1, 10, 1):
        if (numbers.count(i) == 0):
            Not.append(i)
    answer = sum(Not)
    return answer