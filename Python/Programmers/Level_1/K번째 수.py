def solution(array, commands):
    answer = []
    for i in commands:
        save_list = [array[j] for j in range(i[0]-1, i[1], 1)]
        save_list.sort()
        answer.append(save_list[i[2]-1])
    return answer