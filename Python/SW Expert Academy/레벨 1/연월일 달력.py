T = int(input())

for i in range(1, T+1):
    testCase = input()
    if int(testCase[4:6]) <= 0 or int(testCase[4:6]) > 12:
        print("#%d -1" %(i))
    else:
        if int(testCase[4:6]) == 2 and int(testCase[6:8]) > 28:
            print("#%d -1" %(i))
        else:
            print("#%d %s/%s/%s" %(i, testCase[0:4], testCase[4:6], testCase[6:8]))
