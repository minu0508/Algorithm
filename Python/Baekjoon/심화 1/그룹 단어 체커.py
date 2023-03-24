a = int(input())
e = 0

for _ in range(0, a, 1):
    b = list(map(str, input()))
    f = 0
    for i in range(0, len(b)-2, 1):
        d = []
        if b[i] != b[i+1]:
            d = b[i+1:]
            for j in range(0, len(d), 1):                
                if d[j] == b[i]:
                    f += 1
                else:
                    f += 0
    if f == 0:
        e += 1
    else:
        e += 0

print(e)