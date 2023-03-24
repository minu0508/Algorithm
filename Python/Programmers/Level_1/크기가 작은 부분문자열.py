def solution(t, p):
    answer = 0
    t = list(t)

    for i in range(0, len(t) - (len(p) - 1), 1):
        Str_num = ''
        for j in range(i, i + (len(p)), 1):
            Str_num += t[j]

        if (int(Str_num) <= int(p)):
            answer += 1

    return answer