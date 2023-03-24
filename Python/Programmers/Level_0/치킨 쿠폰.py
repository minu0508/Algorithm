def solution(chicken):
    answer = 0
    coupon = 0

    while(chicken >= 10):
        coupon = chicken // 10
        answer += coupon
        chicken = (chicken % 10) + coupon
    
    return answer