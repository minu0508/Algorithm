def solution(phone_number):
    answer = ''
    phone_number = list(str(phone_number))
    for i in range(0, len(phone_number)-4, 1):
        phone_number[i] = '*'
        
    for j in phone_number:
        answer += j
    return answer