N = int(input())
A = list(map(int, input().split()))
C = 0

for i in A:
    B = 0
    for j in range(2, i+1, 1):
        if i%j == 0:
            B += 1
        else:
            B += 0
    if B == 1:
        C += 1
    
print(C)