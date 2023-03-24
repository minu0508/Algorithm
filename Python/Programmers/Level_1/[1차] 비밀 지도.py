def solution(n, arr1, arr2):
    answer = []
    arr1_list = []
    arr2_list = []
    
    for ar1 in range(n):
        bin_arr1 = list(bin(arr1[ar1]))
        Save_arr1 = (bin_arr1[2:])
        
        if (len(Save_arr1) < n):
            for _ in range(0, n - len(Save_arr1), 1):
                Save_arr1.insert(0, '0')
        arr1_list.append(Save_arr1)
    
    for ar2 in range(n):
        bin_arr2 = list(bin(arr2[ar2]))
        Save_arr2 = (bin_arr2[2:])
        
        if (len(Save_arr2) < n):
            for _ in range(0, n - len(Save_arr2), 1):
                Save_arr2.insert(0, '0')
        arr2_list.append(list(Save_arr2))
    
    for i in range(n):
        total = ""
        for j in range(n):
            if (arr1_list[i][j] == "1" and arr2_list[i][j] == "1"):
                total += "#"
            elif (arr1_list[i][j] != arr2_list[i][j]):
                total += "#"
            elif (arr1_list[i][j] == '0' and arr2_list[i][j] == '0'):
                total += " "
        answer.append(total)
    return answer