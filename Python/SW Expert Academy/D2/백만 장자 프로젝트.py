T = int(input())
for i in range(T):
    N = int(input())
    profit = 0
    maxNum = 0
    arrNum = list(map(int, input().strip().split()))
    for key in arrNum[::-1]:
        if key >= maxNum:
            maxNum = key
        else:
            profit += (maxNum - key)
    print(f"#{i+1} {profit}")