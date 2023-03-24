def solution(common):
    answer = 0
    save_num = []

    for i in range(len(common) - 1):
        save_num.append(common[i+1] - common[i])

    save_num = list(set(save_num))

    if (len(save_num) == 1):
        answer = common[len(common)-1] + save_num[0]
    else:
        answer = common[len(common)-1] * (common[len(common)-1] // common[len(common)-2])
    return answer