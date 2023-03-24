def solution(dots):
    answer = 0
    dots_x = []
    dots_y = []

    for i in dots:
        dots_x.append(i[0])
        dots_y.append(i[1])
        
    answer = (max(dots_x) - min(dots_x)) * (max(dots_y) - min(dots_y))

    return answer