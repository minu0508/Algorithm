T = int(input())
number_list = list(map(int, input().split()))
number_list.sort()

print(number_list[T // 2])