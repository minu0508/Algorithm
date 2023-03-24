a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []

if len(c) == a:
    for i in range(0, a, 1):
        if (b > c[i]):
            d.append(c[i])          
else:
    print("N의 길이와 수열의 개수가 맞지 않으니 다시 시작하세요.")

for j in range(0, len(d), 1):
    print(d[j], end = ' ')