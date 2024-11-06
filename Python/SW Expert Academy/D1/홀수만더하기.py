T = int(input())

for i in range(T):
    answer = 0
    number_list = list(map(int, input().split()))
    for j in number_list:
        if (j % 2 == 1):
            answer += j

    print("#%d %d" %(i+1, answer))