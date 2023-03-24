def solution(numlist, n):
    answer = []
    minus = []
    distance = []
    
    for i in numlist:
        minus.append(i - n)

    for j in numlist:
        if (j - n >= 0):
            distance.append(j - n)
        else:
            distance.append(abs(j-n))
    distance = sorted(distance)

    for k in range(0, len(distance)-1, 1):
        if (distance[k] == distance[k+1]):
            distance[k+1] = -distance[k+1]
    

    for l in range(0, len(distance), 1):
        if (minus.count(distance[l]) == 0):
            distance[l] *= -1

    for num in distance:
        answer.append(num + n)
    print(answer)
    
    return answer

solution([10000, 20, 36, 47, 40, 7, 10, 7000], 30)