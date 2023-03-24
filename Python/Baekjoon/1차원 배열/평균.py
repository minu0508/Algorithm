a = int(input())
b = list(map(int, input().split()))
c = max(b)
d = []
e = 0

for i in b:
    d.append(i/c*100)

for j in range(0, len(d), 1):
    e += d[j]

print(e/a)