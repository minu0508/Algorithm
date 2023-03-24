kg = int(input())
bongtoo = 0

while True:
    if kg%5 == 0:
        bongtoo = bongtoo + (kg//5)
        print(bongtoo)
        break
    elif kg < -1:
        print(-1)
        break
    
    kg -= 3
    bongtoo += 1