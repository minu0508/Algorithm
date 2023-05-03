def solution(num_list):
    even = 0
    odd = 0
    
    for i in range(0, len(num_list), 1):
        if (i % 2 == 0):
            odd += num_list[i]
        else:
            even += num_list[i]
    
    if (odd > even):
        return odd
    else:
        return even