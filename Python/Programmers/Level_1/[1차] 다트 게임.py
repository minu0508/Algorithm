def solution(dartResult):
    answer = 0
    dartResult = [__ for __ in dartResult]
    number = [str(_) for _ in range(0, 11, 1)]
    String = ["S", "D", "T"]
    total = []
    Save_Num = 0
    step = 0

    for i in range(0, len(dartResult), 1):
        if (number.count(dartResult[i]) >= 1):
            Save_Num = int(dartResult[i])
            step += 1
            if (dartResult[i-1] == "1"):
                Save_Num += 10
        
        elif (String.count(dartResult[i]) >= 1):
            if (dartResult[i] == "S"):
                Save_Num *= 1
                total.append(Save_Num)
                Save_Num = 0
            elif (dartResult[i] == "D"):
                Save_Num *= Save_Num
                total.append(Save_Num)
                Save_Num = 0
            else:
                Save_Num = Save_Num * Save_Num * Save_Num
                total.append(Save_Num)
                Save_Num = 0


        elif (dartResult[i] == "*"):
            if (step == 1):
                total[0] *= 2
            else:
                for j in range(step-2, step, 1):
                    total[j] *= 2
        elif (dartResult[i] == "#"):
            total[step-1] *= -1

    return answer