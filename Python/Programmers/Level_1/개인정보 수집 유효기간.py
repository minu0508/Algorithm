def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    Plus_period = {}
    index = 1
    
    for t in terms:
        t = t.split(" ")
        Plus_period[t[0]] = int(t[1])
        
    print(Plus_period)
        
    for p in privacies:
        date = []
        Plus_year = 0
        
        Save_1 = p.split(" ")
        Save_2 = Save_1[0].split(".")
        Save_3 = int(Save_2[1]) + Plus_period.get(Save_1[1])
        
        while (True):
            if (Save_3 > 12):
                Plus_year += 1
                Save_3 -= 12
            else:
                break
            
        year = int(Save_2[0]) + Plus_year
        day = int(Save_2[2]) - 1
        
        if (day == 0):
            day = 28
            Save_3 -= 1
            
        date = [year, Save_3, day]
        
        if (today[0] > date[0]):
            answer.append(index)
            
        elif (today[0] == date[0] and today[1] > date[1]):
            answer.append(index)
        
        elif (today[0] == date[0] and today[1] == date[1] and today[2] > date[2]):
            answer.append(index)
            
        index += 1
    return answer