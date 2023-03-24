def solution(k, m, score):
    answer = 0
    score.sort()

    for i in range(len(score) // m):
        Save_Box = []
        for j in range(0, m, 1):
            Save_Box.append(score[-1])
            score.pop()
        answer += min(Save_Box) * m
        
    return answer