a = int(input())
e = []
g = []

for i in range(0, a, 1):
    d = []
    b, c = list(input().split())
    for j in c:
        d.append(j*int(b))
    f = d[0]
    for k in range(1, len(d), 1):
        e = d[k]
        f += e
    g.append(f)

for l in range(0, len(g), 1):
    print(g[l])