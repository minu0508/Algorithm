a = int(input())
d = []
for i in range(0, a, 1):
    b, c = map(int, input().split())
    d.append(b+c)
    
for j in range(0, a, 1):
    print(d[j])