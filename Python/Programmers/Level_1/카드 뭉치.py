def solution(cards1, cards2, goal):
    answer = "Yes"
    for i in goal:
        if (len(cards1) >= 1 and len(cards2) >= 1):
            if i == cards1[0]:
                cards1.pop(0)
            elif i == cards2[0]:
                cards2.pop(0)
            else:
                return "No"
        elif (len(cards1) >= 1 and len(cards2) == 0):
            if i == cards1[0]:
                cards1.pop(0)
            else:
                return "No"
        elif (len(cards2) >= 1 and len(cards1) == 0):
            if i == cards2[0]:
                cards2.pop(0)
            else:
                return "No"
    return answer