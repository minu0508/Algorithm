A = int(input())
B = list(map(int, input()))
C = 1
total = 0

for i in range(len(B)-1, -1, -1):
    print(A * B[i])
    total = total + (A*(B[i] * C))
    C *= 10
    
print(total)