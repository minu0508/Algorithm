h, m = map(int, input().split())
sec = 45

if (m < 45):
    h -= 1
    if(h < 0):
        h = 23
        sec -= m
        m = 60 - sec
        print("%d %d" % (h, m))
    elif(h >= 0):
        sec -= m
        m = 60 - sec
        print("%d %d" % (h, m))
    
else:
    m -= 45
    print("%d %d" % (h, m))