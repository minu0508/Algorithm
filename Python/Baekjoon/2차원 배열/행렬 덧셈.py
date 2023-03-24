N = list(map(int, input().split()))
AB_1 = []
AB_2 = []

for i in range(N[0]):
    AB_1.append(list(map(int, input().split())))

for j in range(N[0]):
    AB_2.append(list(map(int, input().split())))

for k in range(N[0]):
    for l in range(N[1]):    
        print(AB_1[k][l] + AB_2[k][l], end = ' ')
    print()