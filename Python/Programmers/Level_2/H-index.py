def solution(citations):
    citations.sort()
    length = len(citations)
    
    for i in range(0, length, 1):
        if (citations[i] >= length - i):
            return length - i
    return 0