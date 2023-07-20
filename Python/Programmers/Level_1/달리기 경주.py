def solution(players, callings):
    playersGrade = {}
    answer = []
    
    for i, j in enumerate(players):
        playersGrade[j] = i
    
    for i in callings:
        UpGrade, DownGrade = playersGrade[i] - 1, playersGrade[i]
        players[UpGrade], players[DownGrade] = players[DownGrade], players[UpGrade]
        playersGrade[players[UpGrade]], playersGrade[players[DownGrade]] = playersGrade[players[UpGrade]] - 1, playersGrade[players[DownGrade]] + 1 
    
    playersGrade = sorted(playersGrade.items(), key=lambda x: x[1])
    for i in range(len(playersGrade)):
        answer.append(playersGrade[i][0])
        
    return answer