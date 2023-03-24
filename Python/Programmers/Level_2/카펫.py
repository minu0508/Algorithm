def solution(brown, yellow):
    Save = []
    Total = brown + yellow

    for i in range(1, int(Total ** (1 / 2)) + 1):
        if (Total % i == 0):
            Save.append(i)
            if (i ** 2 != Total):
                Save.append(Total // i)
    Save.sort()

    if (len(Save) % 2 != 0):
        width, height = len(Save) // 2, len(Save) // 2
    else:
        width, height = len(Save) // 2, (len(Save) // 2 - 1)
    print(width, height)
    while (True):
        if ((Save[width] - 2) * (Save[height] - 2) == yellow):
            return [Save[width], Save[height]]
        else:
            width += 1 
            height -= 1