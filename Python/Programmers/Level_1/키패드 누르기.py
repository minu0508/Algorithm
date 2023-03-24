def solution(numbers, hand):
    answer = ''
    dic = {1 : [0, 0], 2 : [1, 0], 3 : [2, 0], 4 : [0, 1], 5 : [1, 1], 6 : [2, 1], 7 : [0, 2], 8 : [1, 2], 9 : [2, 2], '*' : [0, 3], 0 : [1, 3], '#' : [2, 3]}
    R_hand = dic['*']
    L_hand = dic['#']
    
    for i in range(0, len(numbers), 1):
        Present = dic[numbers[i]]
        if (numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7):
            L_hand = Present
            answer += "L"
        
        elif (numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9):                
            R_hand = Present
            answer += "R"
        
        elif (numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0):
            dist_L, dist_R = 0, 0
            
            for j in range(2):
                dist_L += abs(L_hand[j] - Present[j])
                dist_R += abs(R_hand[j] - Present[j])
            
            
            if (dist_L < dist_R):
                L_hand = Present
                answer += "L"
                
            elif (dist_L > dist_R):
                R_hand = Present
                answer += "R"
            
            else:
                if (hand == "left"):
                    L_hand = Present
                    answer += "L"
                else:
                    R_hand = Present
                    answer += "R"
            
    return answer