def solution(sides):
    answer = 0
    Total = 0
    sides = sorted(sides)
    
    for i in range(0, len(sides)-1, 1):
        Total += sides[i]
    
    if (sides[len(sides) - 1] >= Total):
        answer = 2
    else:
        answer = 1
        
    return answer