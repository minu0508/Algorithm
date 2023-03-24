def solution(keymap, targets):
    answer = [0] * len(targets)
    num_index = []
    num = 0
    for i in targets:
        for j in range(len(i)):
            num_index = []
            for k in range(len(keymap)):
                if (keymap[k].count(i[j]) >= 1):
                    num_index.append(keymap[k].index(i[j]) + 1)
                else:
                    pass
            if (len(num_index) == 0):
                answer[num] = -1
                break
            else:
                answer[num] += min(num_index)
        num += 1
    return answer