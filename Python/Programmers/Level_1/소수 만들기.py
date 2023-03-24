def solution(nums):
    answer = 0
    
    for i in range(0, len(nums), 1):
        for j in range(i+1, len(nums), 1):
            for k in range(j+1, len(nums), 1):
                num = nums[i] + nums[j] + nums[k]
                save = 0
                for l in range(2, num, 1):
                    if (num % l == 0):
                        save = 0
                        break
                    else:
                        save = 1
                        
                if (save == 1):
                    answer += 1
    return answer