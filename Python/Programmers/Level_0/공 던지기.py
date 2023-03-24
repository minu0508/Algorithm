def solution(numbers, k):
    answer = 0
    Num = 2 * (k-1)
    while(True):
        if (Num > len(numbers)):
            Num -= len(numbers)
        else:
            break
            
    answer = numbers[Num]
    return answer