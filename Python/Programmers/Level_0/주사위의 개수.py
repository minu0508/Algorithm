def solution(box, n):
    answer = 0
    
    for i in range(0, len(box), 1):
        box[i] = box[i] - (box[i] % n)
        
    n = n*n*n
    answer = (box[0]*box[1]*box[2]) // n 
    return answer