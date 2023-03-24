a = list(input().upper())
c = []

if len(a) == 1:
    print(a[0])

else:
    for i in sorted(set(a)):
        b = []
        b.append(i)
        b.append(a.count(i))
        c.append(b)

    c.sort(key = lambda x : x[1])

    for _ in range(0, len(c) - 2, 1):
        c.remove(c[0])

    d = list(c[0])
    f = list(c[1])

    if d[1] == f[1]:
        print("?")
    elif d[1] < f[1]:
        print(f[0])