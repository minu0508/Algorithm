def solution(s):
    x_count = 1
    The_rest = 0
    x = s[0]
    Save = [] 
    Word = ""
    Word += s[0]

    for i in range(1, len(s)-1, 1):
        if (x == s[i]):
            x_count += 1
            Word += s[i]
        elif (x != s[i]):
            The_rest += 1
            Word += s[i]
        
        if (x_count == The_rest):
            Save.append(Word)
            x_count = 0
            The_rest = 0
            Word = ""
            x = s[i+1]

    if (x_count != The_rest):
        Word += s[len(s)-1]
        Save.append(Word)
    else:
        Save.append(s[len(s)-1])
    return len(Save)