def solution(my_str, n):
    my_str = list(str(my_str))
    answer = []
    Save_Word = ''
    Save_Number = 0
    Save = n
    
    while(True):
        try:
            Save_Word += my_str[Save_Number]
            Save_Number += 1
        except:
            pass
        
        if (Save_Number % n == 0 or Save_Number == len(my_str)):
            answer.append(Save_Word)
            Save_Word = ''
            n += Save
            if (Save_Number == len(my_str)):
                break
    return answer