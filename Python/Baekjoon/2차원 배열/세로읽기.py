textList = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

for i in range(1, 6, 1):
    inputText = list(input())
    for j in range(0, len(inputText), 1):
        textList[j] += inputText[j]
    
print(''.join(textList))