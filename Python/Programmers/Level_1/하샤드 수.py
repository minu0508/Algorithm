def solution(x):
    X = list(str(x))
    Total = 0
    
    for i in range(0, len(X), 1):
        Total += int(X[i])
        
    if (x % Total == 0):
        return True
    else:
        return False