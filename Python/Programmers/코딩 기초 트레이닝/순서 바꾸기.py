def solution(num_list, n):
    answer = [num_list[i] for i in range(n, len(num_list), 1)]
    for i in range(n):
        answer.append(num_list[i])
    return answer