def solution(n, lost, reserve):
    answer = 0

    Student = [1] * (n + 2)
    Lost_Student = [1 if i in lost else 0 for i in range(n+2)]
    Reserve_student = [1 if j in reserve else 0 for j in range(n+2)]
    Total_Student = [Student[k] - Lost_Student[k] + Reserve_student[k] for k in range(n+2)]

    for _ in range(1, n + 1, 1):
        if (Total_Student[_] > 1 and Total_Student[_ - 1] == 0):
            Total_Student[_] -= 1
            Total_Student[_ - 1] += 1
        if (Total_Student[_] > 1 and Total_Student[_ + 1] == 0):
            Total_Student[_] -= 1
            Total_Student[_ + 1] += 1
            
    answer = n - Total_Student.count(0)

    return answer