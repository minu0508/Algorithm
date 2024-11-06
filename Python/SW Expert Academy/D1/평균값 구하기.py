T = int(input())

for i in range(T):
    number_list = list(map(int, input().split()))
    answer = sum(number_list) / len(number_list)

    print("#%d %d" %(i+1, round(answer)))