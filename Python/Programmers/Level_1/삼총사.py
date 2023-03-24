def solution(number):
    answer = 0
    count = 0
    for i in range(0, len(number), 1):
        for j in range(i+1, len(number), 1):
            for k in range(j+1, len(number), 1):
                if (number[i] + number[j] + number[k] == 0):
                    count += 1
            
    return count