def solution(polynomial):
    answer = ''
    Plus = 0
    num = 0
    Save = []
    polynomial = list(polynomial.split(" + "))
    
    for i in polynomial:
        if (i.count('x') == 1):
            Save.append(i)
        else:
            num += int(i)

    for j in range(len(Save)):
        if (len(Save[j]) >= 2):
            Plus += int(Save[j][:-1])
        else:
            Plus += 1
    
    if (Plus >= 2):
        if (int(num) >= 1):
            answer = str(Plus) + 'x + ' + str(num)
        else:
            answer = str(Plus) + 'x'        
    elif (Plus == 1):
        if (int(num) >= 1):
            answer = 'x + ' + str(num)
        else:
            answer = 'x'
    else:
        answer += str(num)
    return answer