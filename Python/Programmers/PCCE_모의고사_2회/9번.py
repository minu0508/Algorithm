def solution(serial):
    answer = ''
    serialList = [[serial[i], serial[i+1]] for i in range(0, len(serial), 2)]
    dict = {'0' : 'operation', '1' : 'sales', '2' : 'develop', '3' : 'finance', '4' : 'law', '5' : 'research'}
    
    answer += 'male/' if (serialList[0][1] == '1') else 'female/'
    answer += dict[serialList[1][1]] + '/'
    answer += serialList[2][1] + 'team/' if (serialList[2][0] == '0') else serialList[2][0] + serialList[2][1] + 'team/'
    serialPlus = [int(serial[j]) for j in range(0, len(serial) - 2, 1)]
    answer += 'valid' if(sum(serialPlus) % 13 == int(serial[len(serial) - 2:])) else 'invalid'
    return answer