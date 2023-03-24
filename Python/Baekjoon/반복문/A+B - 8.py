T = int(input())
D = [0]
E = [0]
F = [0]

for _ in range(0, T, 1):
    A, B = map(int, input().split())
    E.append(A)
    F.append(B)
    D.append(A+B)
     
for i in range(1, (T+1), 1):
    print("Case #%d: %d + %d = %d" %(i, E[i], F[i], D[i]))