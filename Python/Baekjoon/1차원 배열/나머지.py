c = []

for i in range(0, 10, 1):
    a = int(input())
    b = a % 42
    c.append(b)

c = list(set(c))
print(len(c))