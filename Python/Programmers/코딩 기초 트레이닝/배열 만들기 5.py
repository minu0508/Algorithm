def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        i = i[s:s+l]
        if (int(i) > k):
            answer.append(int(i))
    return answer