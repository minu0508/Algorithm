def solution(nums):
    answer = 0
    mon = len(nums) // 2
    kind_nums = list(set(nums))
    if (len(kind_nums) > mon):
        answer = mon
    elif (len(kind_nums) < mon):
        answer = len(kind_nums)
    else:
        answer = mon
    
    return answer