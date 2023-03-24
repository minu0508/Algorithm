def solution(num, total):
    answer = []
    Plus = 0
    difference = 0

    for i in range(num+1):
        Plus += i

    difference = total - Plus 
    first_num = (difference // num) + 1
    
    for j in range(num):
        answer.append(j + first_num)

    return answer