def solution(my_string):
    answer = []
    Num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        for j in Num_list:
            if (i == j):
                answer.append(int(i))
    answer.sort()
    return answer