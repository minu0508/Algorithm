def solution(price, money, count):
    answer = 0
    Total = 0
    
    for i in range(1, count+1, 1):
        Total += (price * i)
    
    if (Total <= money):
        answer = 0
    elif (Total > money):
        answer = Total - money
    return answer