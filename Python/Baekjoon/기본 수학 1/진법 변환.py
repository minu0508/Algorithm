# 65 ~ 90

inputText = list(input().split())
numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
answer = 0

firstInputList = list(reversed(inputText[0]))
print(firstInputList)

for i in range(len(firstInputList)-1, -1, -1):
    if (numberList.count(firstInputList[i]) == 1):
        answer += int(firstInputList[i]) * (int(inputText[1]) ** i)
        print(answer)
    else:
        answer += (ord(firstInputList[i]) - 55) * (int(inputText[1]) ** i)
    # answer += (ord(inputAlphaAndNumber[0][i]) - 55) * int(inputAlphaAndNumber[1])**i
    
print(answer)