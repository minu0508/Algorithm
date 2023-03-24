Basket_size, Step = map(int, input().split())
Basket = ['0'] * Basket_size

for i in range(Step):
    ball = list(map(int, input().split()))
    for j in range(ball[0] - 1, ball[1], 1):
        Basket[j] = str(ball[2])

answer = ' '.join(Basket)
print(answer)