T = int(input())
D = [0]

for _ in range(0, T, 1):
    A, B = map(int, input().split())
    D.append(A+B)
    
for i in range(1, (T+1), 1):
    print("Case #%d: %d" %(i, D[i]))    