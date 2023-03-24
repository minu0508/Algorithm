def solution(babbling):
    answer = 0
    shout = ['aya', 'ye', 'woo', 'ma']
    Save_list = []

    for i in babbling:
        for j in shout:
            i = i.replace(j, "*")
        Save_list.append(i)

    for k in Save_list:
        star = 0
        if (len(k) == 1):
            if (k == "*"):
                answer += 1
        else:
            for l in k:
                if (l == "*"):
                    star += 1
            if (star == len(list(k))):
                answer += 1

    return answer