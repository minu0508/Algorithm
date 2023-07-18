def solution(name, yearning, photo):
    answer = []
    nameDict = {}
    for i in range(len(name)):
        nameDict[name[i]] = yearning[i]
        
    for i in photo:
        longing = 0
        for j in range(len(i)):
            if (name.count(i[j]) == 1):
                longing += nameDict[i[j]]
            else:
                pass
        answer.append(longing)
    return answer