c = []

while True:
    a, b = map(int, input().split())
    c.append(a+b)

    if ( a==0 and b==0):
        break

for i in range(0, len(c)-1, 1):
    print(c[i])