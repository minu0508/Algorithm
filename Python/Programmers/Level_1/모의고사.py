def solution(answers):
    answer = []
    score = [0 , 0, 0]
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    step = 0
        
    for i in answers:
        if (person_1[step % len(person_1)] == i):
            score[0] += 1
        if (person_2[step % len(person_2)] == i):
            score[1] += 1
        if (person_3[step % len(person_3)] == i):
            score[2] += 1
        step += 1
        
    for j in range(len(score)):
        if (max(score) == score[j]):
            answer.append(j + 1)    
            
    return answer