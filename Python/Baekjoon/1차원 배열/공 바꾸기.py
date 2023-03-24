N, M = map(int, input().split())
Basket = [str(_) for _ in range(1, N + 1, 1)]

for _ in range(M):
    i, j = map(int, input().split())
    Save = Basket[i - 1]
    Basket[i - 1] = Basket[j - 1]
    Basket[j - 1] = Save

answer = ' '.join(Basket)
print(answer)