def solution(arr):
    stk = []
    for i in range(0, len(arr), 1):
        if(len(stk) == 0):
            stk.append(arr[i])
        else:
            if (stk[-1] == arr[i]):
                stk.pop()
            else:
                stk.append(arr[i])
    
    if (len(stk) == 0):
        return [-1]
    else:
        return stk