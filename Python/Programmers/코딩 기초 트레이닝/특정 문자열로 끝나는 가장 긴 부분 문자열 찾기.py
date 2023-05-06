def solution(myString, pat):
    answer = ''
    myString = myString.replace(pat, "-")
    for i in range(len(myString)-1, -1, -1):
        if (myString[i] == "-"):
            break
    myString = myString[:i+1].replace("-", pat)
    return myString