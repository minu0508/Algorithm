def solution(rank, attendance):
    answer = 0
    grade = []
    
    for i in range(len(attendance)):
        if (attendance[i] == True):
            grade.append(rank[i])
    grade.sort()
    answer = rank.index(grade[0]) * 10000 + rank.index(grade[1]) * 100 + rank.index(grade[2])
    return answer