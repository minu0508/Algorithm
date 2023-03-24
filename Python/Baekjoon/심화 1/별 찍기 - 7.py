N = int(input())
star = 1

for i in range(N):
    print(" " * (N - (i + 1)) + "*" * star)
    star += 2
star -= 4

for j in range(((2 * N) - 1) - N):
    print (" " * (j + 1) + "*" * star)
    star -= 2