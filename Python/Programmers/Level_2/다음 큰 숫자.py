def solution(n):
    answer = 0
    N_Bin = bin(n)[2:]
    One_Count = N_Bin.count("1")

    while(True):
        n += 1
        if (bin(n)[2:].count("1") == One_Count):
            answer = n
            break
   
    return answer