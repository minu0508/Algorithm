import string, re

def solution(new_id):
    answer = ''
    len_zero_answer = ''
    new_id = list(new_id)
    alpha = list(string.ascii_lowercase)
    number = [str(_) for _ in range(0, 10, 1)]
    emotion = ['-', '_', '.']

    for i in range(len(new_id)):
        new_id[i] = new_id[i].lower()
        if (alpha.count(new_id[i]) != 0 or number.count(new_id[i]) != 0 or emotion.count(new_id[i]) != 0):
            answer += new_id[i]
    answer = re.sub(r"[.]+", ".", answer)
    Save = list(answer)

    if (len(answer) >= 3):
        if (answer[0] == "."):
            del Save[0]
        if (answer[-1] == "."):
            del Save[-1]
    if (len(answer) == 1):
        if (answer[0] == "."):
            del Save[0]

    if (len(Save) == 0):
        len_zero_answer += "a"
        while(len(len_zero_answer) < 3):
            len_zero_answer += "a"
        return len_zero_answer
    
    elif (len(Save) > 15):
        Save = Save[:15]
        if (Save[-1] == "."):
            del Save[-1]
        if (Save[0] == "."):
            del Save[0]
        answer = ''.join(Save)
        return answer
    
    elif (len(Save) < 3):
        while (len(Save) < 3):
            Save.append(Save[len(Save)-1])
        answer = ''.join(Save)
        return answer
    else:
        answer = ''.join(Save)
        return answer