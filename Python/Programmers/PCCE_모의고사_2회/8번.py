def solution(num_list):
    for n in num_list:
        for i in range(0, len(num_list) - 1, 1):
            if (num_list[i] > num_list[i + 1]):
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

    return num_list