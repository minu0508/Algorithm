def solution(myString, pat):
    answer = ''
    for i in range(len(myString)):
        if (myString[i] == 'A'):
            answer += "B"
        else:
            answer += "A"
    
    if (answer.count(pat) >= 1):
        return 1
    else:
        return 0