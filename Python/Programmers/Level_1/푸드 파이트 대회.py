def solution(food):
    answer = ''
    for i in range(0, len(food), 1):
        if (food[i] // 2 >= 1):
            for j in range(0, food[i] // 2, 1):
                answer += str(i)
    save_answer = list(answer)
    save_answer.reverse()
    answer += '0'
    for k in save_answer:
        answer += str(k)

    return answer