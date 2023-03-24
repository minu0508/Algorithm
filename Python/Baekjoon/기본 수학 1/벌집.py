A = int(input())
B = 1
C = 6
D = 1

if A == 1:
    print(1)

else:
    while True:
        B += C
        D += 1
        if A <= B:
            print(D)
            break
        C += 6