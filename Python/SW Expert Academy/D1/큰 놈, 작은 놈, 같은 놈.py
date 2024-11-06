T = int(input())

for i in range(T):
    number_list = list(map(int, input().split()))
    if (number_list[0] > number_list[1]):
        print("#%d >" %(i+1))
    elif (number_list[0] < number_list[1]):
        print("#%d <" %(i+1))
    elif (number_list[0] == number_list[1]):
        print("#%d =" %(i+1))