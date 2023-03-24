def solution(array, n):
    answer = 0
    Num = 0
    Result = []
    array.sort()
    
    for i in range(len(array)):
        Num = abs(n - array[i])
        Result.append(Num)
    
    answer = array[Result.index(min(Result))]
    return answer