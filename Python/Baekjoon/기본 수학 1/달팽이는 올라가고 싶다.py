A, B, V = list(map(int, input().split()))
day = (V-B)/(A-B)
print(int(day) if day == int(day) else int(day) + 1)