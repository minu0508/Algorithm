def solution(d, budget):
    d.sort()
    while (True):
        if sum(d) > budget:
            d.pop()
        else:
            return len(d)