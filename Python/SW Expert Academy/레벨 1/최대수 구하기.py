T = int(input())

for i in range(T):
    number_list = list(map(int, input().split()))
    print("#%d %d" %(i+1, max(number_list)))