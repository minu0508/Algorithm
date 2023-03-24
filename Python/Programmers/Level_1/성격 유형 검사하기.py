def solution(survey, choices):
    answer = ''
    Score_list = [0] * 8
    KBTI = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']

    for i in range(len(survey)):
        if (choices[i] > 4):
            Score_list[KBTI.index(survey[i][1])] += choices[i] - 4
        elif (choices[i] < 4):
            Score_list[KBTI.index(survey[i][0])] += 4 - choices[i]
    
    for j in range(0, len(Score_list)-1, 2):
        Save = [KBTI[j], KBTI[j + 1]]
        Save.sort()
        if (Score_list[j] > Score_list[j + 1]):
            answer += KBTI[j]
        elif (Score_list[j] < Score_list[j + 1]):
            answer += KBTI[j + 1]
        else:
            answer += Save[0]
    return answer