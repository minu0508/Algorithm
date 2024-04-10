def solution(array):
    answer = 0
    count_list = []
    Max_number = 0
    array_set = list(set(array))

    if (len(array) == 1):
        answer = array[0]
    else:
        for i in array_set:
            count_list.append(array.count(i))
        Max_number = max(count_list)

        if (count_list.count(Max_number) > 1):
            answer = -1
        else:
            answer = array_set[count_list.index(Max_number)]

    return answer

# 24-04-10
def solution(array):
    numDict = {str(i) : 0 for i in array}
    
    for i in array:
        numDict[str(i)] += 1
    valuesList = list(numDict.values())
    
    if (valuesList.count(max(valuesList)) > 1):
        return -1
    else:
        for i in numDict:
            if (numDict[i] == max(valuesList)):
                return i
