from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cacheList = deque([])

    if (cacheSize == 0):
        answer = len(cities) * 5

    else:
        for i in cities:
            i = i.lower()
            if (cacheList.count(i) != 1):
                cacheList.append(i)
                answer += 5
                if (len(cacheList) > cacheSize):
                    cacheList.popleft()
            else:
                cacheList.remove(i)
                cacheList.append(i)
                answer += 1
                if (len(cacheList) > cacheSize):
                    cacheList.popleft()
    return answer