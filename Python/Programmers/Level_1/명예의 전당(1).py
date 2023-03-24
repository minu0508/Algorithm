def solution(k, score):
    answer = []
    honor = []
    min_score = 0

    for i in score:
        honor.append(i)
        if (len(honor) > k):
            honor = sorted(honor, reverse=True)
            honor.pop()
            min_score = min(honor)
        else:
            min_score = min(honor)
        answer.append(min_score)
    
    return answer