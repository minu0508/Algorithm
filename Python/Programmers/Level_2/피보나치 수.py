def solution(n):
    step = [0, 1]

    if (n == 2):
        return step[n] % 1234567
    else:
        for _ in range(1, n, 1):
            step.append(step[-1] + step[-2])
        return step[n] % 1234567