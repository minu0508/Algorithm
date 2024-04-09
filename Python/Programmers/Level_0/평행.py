def solution(dots):
    num = []
    for i in range(len(dots)):
        for j in range(i+1, len(dots), 1):
            if (int(dots[i][1] - dots[j][1]) != 0.0):
                num.append((int(dots[i][0] - dots[j][0])) / (int(dots[i][1] - dots[j][1])))
            else:
                pass
    for k in num:
        if num.count(k) >= 2:
            return 1
    else:
        return(0)

# 24-04-09
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    
    if ((y1 - y2) / (x1 - x2) == (y3 - y4) / (x3 - x4)):
        return 1
    if ((y1 - y3) / (x1 - x3) == (y2 - y4) / (x2 - x4)):
        return 1
    if ((y1 - y4) / (x1 - x4) == (y3 - y2) / (x3 - x2)):
        return 1

    return 0
