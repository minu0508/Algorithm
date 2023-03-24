def solution(n, words):
    answer = []
    Save = []

    for i in range(len(words)):
        Save.append(words[i])

        if (len(Save) >= 2):
            if (Save[i][0] != Save[i - 1][-1]):
                if ((i + 1) % n != 0):
                    answer = [(i + 1) % n, ((i + 1) // n) + 1]
                else:
                    answer = [n, (i + 1) // n]
                break
            elif (Save.count(Save[i]) > 1):
                if ((i + 1) % n != 0):
                    answer = [(i + 1) % n, ((i + 1) // n) + 1]
                else:
                    answer = [n, (i + 1) // n]
                break
            else:
                answer = [0, 0]
    return answer