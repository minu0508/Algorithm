def solution(n):
    step = 1
    answer = 0
    while(True):
        num = step*step
        if step*step == n:
            answer = (step+1) * (step+1)
            break
        elif (num >= n):
            answer = -1
            break
        step += 1
    return answer