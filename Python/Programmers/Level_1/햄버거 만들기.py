def solution(ingredient):
    answer = 0
    Save = []

    for i in range(0, len(ingredient), 1):
        Save.append(ingredient[i])
        if (len(Save) >= 4):
            if (Save[-1] == 1 and Save[-2] == 3 and Save[-3] == 2 and Save[-4] == 1):
                for _ in range(4):
                    Save.pop()
                answer += 1
    return answer