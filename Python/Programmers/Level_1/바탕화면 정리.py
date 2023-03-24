def solution(wallpaper):
    answer = []
    Step_list = []
    Step = 0
    lux, luy, rdx, rdy = 0, 0, 0, 0

    for i in wallpaper:
        if (i.count("#") >= 1):
            num = 0
            for j in range(len(i)):
                if (i[j] == "#"):
                    answer.append(num)
                num += 1
            Step_list.append(Step)
        Step += 1
    
    lux = min(answer)
    luy = min(Step_list)
    rdx = max(answer) + 1
    rdy = max(Step_list) + 1
    return [luy, lux, rdy, rdx]