def solution(a, b, c, d):
    answer, equal, dif = 0, 0, 0
    Save = [a, b, c, d]
    Save_set = list(set(Save)) # set() : 중복 제거
    Trd_list = []
    
    if (len(Save_set) == 1):
        answer = 1111 * Save_set[0]
        
    elif (len(Save_set) == 2):
        for i in Save_set:
            if (Save.count(i) == 2):
                answer = (Save_set[0] + Save_set[1]) * (abs(Save_set[0] - Save_set[1]))
                break
            elif (Save.count(i) == 3):
                equal = i # 
            elif (Save.count(i) == 1):
                dif = i # 1번만 돌아가서 dif == 1
            
            if (equal >= 1 and dif >= 1):
                answer = (10 * equal + dif) * (10 * equal + dif)
                break
                
    elif (len(Save_set) == 3):
        for i in Save_set:
            if (Save.count(i) == 2):
                pass # pass가 good!
            else:
                Trd_list.append(i) # list value == [5, 6]
        answer = Trd_list[0] * Trd_list[1] 
                
    elif (len(Save_set) == 4):
        answer = min(Save_set) # min() : minimal() 즉, 최솟값.
        
    return answer