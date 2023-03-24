def solution(lottos, win_nums):
    answer = []
    score = 0
    fake_score = 0

    for i in range(len(lottos)):
        if (win_nums.count(lottos[i]) >= 1):
            score += 1
        elif (lottos[i] == 0):
            fake_score += 1

    if (score == 2):
        answer.append(5)
        grade = 5
    elif (score == 3):
        answer.append(4)
        grade = 4
    elif (score == 4):
        answer.append(3)
        grade = 3
    elif (score == 5):
        answer.append(2)
        grade = 2
    elif (score == 6):
        for j in range(0, 2, 1):
            answer.append(1)
    else:
        answer.append(6)
        grade = 6

    if (fake_score >= 1):
        Plus_score = fake_score + score
        if (Plus_score == 2):
            answer.append(5)
        elif (Plus_score == 3):
            answer.append(4)
        elif (Plus_score == 4):
            answer.append(3)
        elif (Plus_score == 5):
            answer.append(2)
        elif (Plus_score == 6):
            answer.append(1)

    elif (fake_score == 0 and len(answer) == 1):
        answer.append(grade)
    answer.sort()
    
    return answer