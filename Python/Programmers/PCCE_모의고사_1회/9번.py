def solution(num_list):
    answer = []
    for i in num_list:
        saveList = []
        for j in range(1, i + 1, 1):
            if (i % j == 0):
                saveList.append(j)
                if (len(saveList) > 2):
                    result = False
                    break
                else:
                    result = True
        answer.append(result)
    return answer