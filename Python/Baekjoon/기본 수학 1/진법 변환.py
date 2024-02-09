# 65 ~ 90

inputText = list(input().split())
numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
answer = 0

firstInputList = list(reversed(inputText[0]))

for i in range(len(firstInputList)-1, -1, -1):
    if (numberList.count(firstInputList[i]) == 1):
        answer += int(firstInputList[i]) * (int(inputText[1]) ** i)
    else:
        answer += (ord(firstInputList[i]) - 55) * (int(inputText[1]) ** i)
    
print(answer)
