def solution(myString):
    myString += "x"
    answer = []
    step = 0
    for i in myString:
        if (i == "x"):
            answer.append(step)
            step = 0
        else:
            step += 1
    return answer