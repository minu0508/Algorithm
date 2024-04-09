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

# 24-04-09
def solution(common):
    if (common[2] - common[1] == common[1] - common[0]):
        return common[-1] + (common[2] - common[1])
    else:
        return common[-1] * ((common[2] - common[1]) // (common[1] - common[0]))
