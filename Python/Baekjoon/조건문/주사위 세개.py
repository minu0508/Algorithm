A, B, C = map(int, input().split())
M = 0

if (A == B == C):
    M = 10000 + A*1000
    print(M)

elif (A == B != C or A != B == C or A == C != B):
    if (A==B or A==C):
        M = 1000+(A*100)
    elif (B==C):
        M = 1000+(B*100)
    print(M)

else:
    print(max(A, B, C)*100)