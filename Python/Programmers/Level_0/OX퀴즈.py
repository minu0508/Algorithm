def solution(quiz):
    answer = []
    Math = ''
    Minus = 0
    Plus = 0

    for i in quiz:
        Math = list(i.split())
        
        if (Math.count('-') == 1):
            Minus = int(Math[0]) - int(Math[2])
            if (Minus == int(Math[4])):
                answer.append("O")
            else:
                answer.append("X")
        else:
            Plus = int(Math[0]) + int(Math[2])
            if (Plus == int(Math[4])):
                answer.append("O")
            else:
                answer.append("X")

    return answer

# 24-04-09
def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split(" ")
        if (i.count("-") == 1):
            if (int(i[0]) - int(i[2]) == int(i[4])):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if (int(i[0]) + int(i[2]) == int(i[4])):
                answer.append("O")
            else:
                answer.append("X")
    return answer
