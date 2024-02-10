while(True):
    inputFirstNumber, inputSecondNumber = map(int, input().split())
    
    if ((inputFirstNumber == 0) and (inputSecondNumber == 0)):
        break
    
    else:
        if (inputFirstNumber >= inputSecondNumber):
            if (inputFirstNumber % inputSecondNumber == 0):
                print("multiple")
            else:
                print("neither")
        elif (inputSecondNumber > inputFirstNumber):
            if (inputSecondNumber % inputFirstNumber == 0):
                print("factor")
            else:
                print("neither")