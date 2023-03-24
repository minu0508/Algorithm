t = int(input())
A = 0
B = 0
C = 0
D = []

for _ in range(0, t, 1):
    h, w, n = list(map(int, input().split()))

    if n % h != 0:
        A = n%h
        A *= 100
        B = int(n/h)
        B += 1
        C = A + B
        D.append(C)
    else:
        A = h*100
        B = int(n/h)
        C = A+B
        D.append(C)

for i in range(0, len(D), 1):
    print(D[i])