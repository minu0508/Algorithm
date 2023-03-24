a, b = input().split()
a = list(a)
b = list(b)
c = []
d = []
e = 1000
f = 0

for i in range(len(a)-1, -1, -1):
    f += int(a[i]) * (int(e/10))
    e = int(e / 10)
c.append(f)

f = 0
e = 1000

for j in range(len(b)-1, -1, -1):
    f += int(b[j]) * (int(e/10))
    e = int(e/10)
d.append(f)

if c[0] > d[0]:
    for k in range(0, len(c), 1):
        print(c[k], end = '')
else:
    for k in range(0, len(d), 1):
        print(d[k], end = '')