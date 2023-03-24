def solution(n):
    answer = []
    Num = 2

    while (Num <= n):
        if n % Num == 0:
            answer.append(Num)
            n = n / Num
        else:
            Num += 1
    answer = sorted(list(set(answer)))
    return answer