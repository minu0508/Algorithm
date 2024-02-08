maxNumber = 0
y, x = 0, 0

for i in range(1, 10, 1):
    inputNumber = list(map(int, input().split()))
    if (maxNumber <= max(inputNumber)):
        maxNumber =  max(inputNumber)
        y, x = i, inputNumber.index(max(inputNumber)) + 1
    
print(maxNumber)
print(y, x)