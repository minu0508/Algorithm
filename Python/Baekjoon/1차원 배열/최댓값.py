b = []

for i in range(0, 9, 1):
    a = int(input())
    b.append(a)

print(max(b))

for j in range(0, len(b), 1):
    if max(b) == b[j]:
        print(j+1)