def solution(bandage, health, attacks):
    answer = health
    continuity = 0
    count = 0
    
    for i in range(1, attacks[len(attacks) - 1][0] + 1, 1):
        if (i == attacks[count][0]):
            answer -= attacks[count][1]
            continuity = 0
            count += 1
        else:
            continuity += 1
            answer += bandage[1]
            if (continuity == bandage[0]):
                answer += bandage[2]
                continuity = 0
            
            if (answer >= health):
                answer = health
                
        if (answer <= 0):
            answer = -1
            break
        
    return answer