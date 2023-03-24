def solution(s):
    ''' if(s.count("(") != s.count(")")):
        answer = False
    elif (s[0] == ")"):
        answer = False
    else:
        answer = True
    print(answer) '''

    # 효율성 테스트 실패.
    ''' for i in range(0, len(s) // 2, 1):
        s = s.replace("()", "")
    
    if (len(s) >= 1):
        answer = False
    else:
        answer = True '''
    
    # 3rd Try
    Stack = []
    for i in s:
        if (i == "("):
            Stack.append(i)

        elif ((i == ")" and len(Stack) == 0) or (i == ")" and Stack.pop() != "(")):
            return False
        
    if (Stack):
        return False
    else:
        return True

solution("(())()") # 성공
solution(")()(")
solution("())(")
solution("(()") # 성공