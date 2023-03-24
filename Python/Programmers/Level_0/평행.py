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