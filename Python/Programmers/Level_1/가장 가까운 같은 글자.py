def solution(s):
    answer = []
    
    for i in range(len(s)-1, -1, -1):
        count = 0
        for j in range(i-1, -1, -1):
            if (s[i] == s[j]):
                count += 1
                answer.append(count)
                count = 0
                break
            elif(j == 0):
                answer.append(-1)
            count += 1
    answer.append(-1)
    answer.reverse()
    
    return answer