Discover = list(map(int, input().split()))

Discover[0] = 1 - Discover[0]
Discover[1] = 1 - Discover[1]
Discover[2] = 2 - Discover[2]
Discover[3] = 2 - Discover[3]
Discover[4] = 2 - Discover[4]
Discover[5] = 8 - Discover[5]

for i in range(0, len(Discover), 1):
    print(Discover[i], end = ' ')