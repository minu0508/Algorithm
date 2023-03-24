def solution(numbers):
    numbers.sort()
    arr = []
    answer1 = numbers[0]*numbers[1]
    answer2 = numbers[-1]*numbers[-2]
    arr.append(answer1)
    arr.append(answer2)
    arr.sort(reverse=True)
    
    if (arr[0] > 0):
        answer = arr[0]
    elif (arr[1] > 0):
        answer = arr[1]
    elif (0 in numbers):
        answer = 0
    else:
        answer = arr[0]
        
    return answer