a = int(input())
b = int(input())
c = list(str(b))
d = 0

for i in range(0, len(c), 1):
    d += int(c[i])

print(d)