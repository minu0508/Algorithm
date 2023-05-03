def solution(myString, pat):
    answer = 0
    myString, pat = myString.lower(), pat.lower()
    if (myString.count(pat) >= 1):
        answer = 1
    return answer