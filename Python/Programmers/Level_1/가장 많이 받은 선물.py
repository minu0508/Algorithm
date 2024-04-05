def solution(friends, gifts):
    answer = [0] * len(friends)
    givaAndTake = {i: [0] * len(friends) for i in friends}
    futuresIndex = {i: 0 for i in friends}
    
    for i in gifts:
        i = i.split(" ")
        givaAndTake[i[0]][friends.index(i[1])] += 1
        futuresIndex[i[0]] += 1
        futuresIndex[i[1]] -= 1
    
    for j in friends:
        for k in range(friends.index(j) + 1, len(friends), 1):
            if (j == friends[k]):
                pass
            else:
                if (givaAndTake[j][k] > givaAndTake[friends[k]][friends.index(j)]):
                    answer[friends.index(j)] += 1
                elif (givaAndTake[j][k] < givaAndTake[friends[k]][friends.index(j)]):
                    answer[friends.index(friends[k])] += 1
                elif (givaAndTake[j][k] == givaAndTake[friends[k]][friends.index(j)]):
                    if (futuresIndex[j] > futuresIndex[friends[k]]):
                        answer[friends.index(j)] += 1
                    elif (futuresIndex[j] < futuresIndex[friends[k]]):
                        answer[friends.index(friends[k])] += 1
                    else:
                        pass
    answer = max(answer)
    return answer
