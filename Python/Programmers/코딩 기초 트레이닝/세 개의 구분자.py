def solution(myStr):
    answer = []
    myStr = myStr.replace("a", "-").replace("b", "-").replace("c", "-").split("-")
    for i in myStr:
        if (i == ""):
            pass
        else:
            answer.append(i)
    
    if (len(answer) == 0):
        answer.append("EMPTY")
    return answer