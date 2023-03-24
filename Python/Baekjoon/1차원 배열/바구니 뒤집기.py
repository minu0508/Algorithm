N, M = map(int, input().split())
Basket = [str(_) for _ in range(1, N+1)]

for _ in range(M):
    Save_int = -1
    i, j = map(int, input().split())
    Save = Basket[i-1 : j]
    for k in range(i - 1, j, 1):
        Basket[k] = Save[Save_int]
        Save_int -= 1

answer = ' '.join(Basket)
print(answer)