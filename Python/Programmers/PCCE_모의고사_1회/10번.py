def solution(text, anagram, sw):
    saveText = [""] * len(text)
    if (sw == True):
        for i in range(len(anagram)):
            saveText[anagram[i]] = text[i]
    elif (sw == False):
        for j in range(len(anagram)):
            saveText[j] = text[anagram[j]]
    answer = ''.join(saveText)
    return answer