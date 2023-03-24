import math
def solution(arr):
    answer = 0
    Save = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    Save[0:len(arr)] = arr[0:len(arr)]
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = Save[0], Save[1], Save[2], Save[3], Save[4], Save[5], Save[6], Save[7], Save[8], Save[9], Save[10], Save[11], Save[12], Save[13], Save[14],
    answer = math.lcm(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)
    return answer