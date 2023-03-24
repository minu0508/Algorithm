def solution(score):
    answer = []
    Plus = []
    for i in score:
        Plus.append(i[0] + i[1])

    Plus_Sort = sorted(Plus, reverse=True)

    for j in range(len(Plus_Sort)):
        answer.append(Plus_Sort.index(Plus[j])+1)

    return answer