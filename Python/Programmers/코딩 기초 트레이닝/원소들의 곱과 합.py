def solution(num_list):
    answer = 0
    Save_Mul = 1
    for i in num_list:
        Save_Mul *= i
    Plus = sum(num_list) * sum(num_list)
    
    if (Save_Mul < Plus):
        answer = 1
        
    return answer