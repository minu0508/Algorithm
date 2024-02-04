import collections

inputWord = input().upper()
inputWordCount = collections.Counter(inputWord)
inputWordCountValues = inputWordCount.values()
inputWordMaxCount = max(inputWordCount.values())

totalMax = 0
for i, j in inputWordCount.items():
    if inputWordMaxCount == j:
        totalMax += 1
        if (totalMax >= 2):
            print("?")
            break
    else:
        pass

if totalMax == 1:
    for i, j in inputWordCount.items():
        if inputWordMaxCount == j:
            print(i.upper())
            break