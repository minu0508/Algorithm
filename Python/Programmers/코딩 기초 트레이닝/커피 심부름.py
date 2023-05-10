def solution(order):
    answer = 0
    for i in order:
        if (i.count("latte") >= 1):
            answer += 5000
        elif (i.count("americano") >= 1):
            answer += 4500
        else:
            answer += 4500
    return answer