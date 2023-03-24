A, B = map(int, input().split())
C = int(input())
H = 0
M = 0

if (A < 24):
    if (B+C >= 60):
        H = int((B+C)/60)
        M = int((B+C)%60)
        if (A+H >= 24):
            A = (A+H)-24
            print("%d %d" %(A, M))
        else:
            A += H
            print("%d %d" %(A, M))
    
    elif(B+C < 60):
        M = B+C
        print("%d %d" %(A, M))