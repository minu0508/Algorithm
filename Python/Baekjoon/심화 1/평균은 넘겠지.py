a = int(input())
c = []

for i in range(0, a, 1):
    total = 0
    save = 0
    b = list(map(int, input().split()))
    for j in range(1, len(b), 1):
             total += b[j]
    num = total / b[0]

    for f in range(1, len(b), 1):
        if num < b[f]:
            save += 1
    total = (100 / b[0]) * save
    c.append(total)

for k in range(0, a, 1):
             print("%.3f" %c[k] + "%")