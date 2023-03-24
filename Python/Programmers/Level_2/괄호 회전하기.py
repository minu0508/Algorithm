from collections import deque
def solution(s):
    answer = 0
    saveList = deque(s)
    for i in range(len(s)):
        saveList.append(saveList.popleft())
        save = ""
        for j in saveList:
            save += j
        for _ in range(3):
            save = save.replace("[]", "")
            save = save.replace("()", "")
            save = save.replace("{}", "")
        if (len(save) == 0):
            answer += 1
    return answer

solution("}]()[{")