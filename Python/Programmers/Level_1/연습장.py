a = "...#..##.."
num = 0

for i in range(len(a)):
    num += 1
    if (a[i] == "#"):
        print(num-1)
