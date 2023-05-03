def solution(arr, idx):
    save_arr = arr[idx:]
    
    if (save_arr.count(1) == 0):
        return -1
    else:
        return save_arr.index(1) + idx