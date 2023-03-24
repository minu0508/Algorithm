Total = int(input())
Item = int(input())
Price = 0

for i in range(0, Item, 1):
    Pay = list(map(int, input().split()))

    Price += (Pay[0] * Pay[1])

if (Total == Price):
    print("Yes")
else:
    print("No")