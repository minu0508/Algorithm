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