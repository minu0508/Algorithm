def solution(s):
    Stack = []

    for i in range(len(s)):
        Stack.append(s[i])
        if (len(Stack) >= 2):
            if (Stack[-2] == Stack[-1]):
                for _ in range(2):
                    Stack.pop()

    if (len(Stack) == 0):
        return 1
    else:
        return 0