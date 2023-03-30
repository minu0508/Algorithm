# 딕셔너리로 접근하여 완전히 풀었다.
# 하지만 dict의 value값을 넣는데 count를 썼더니 시간 초과가 떴다.
# 그래서 다른 사람이 dict로 푼 방식을 보니까 그냥 해당 key값에 +1 씩 해주는게
# 시간 복잡도를 더 줄일 수 있는 것을 확인.

# enumerate에 대해서도 새롭게 알게 됨.

def solution(k, tangerine):
    dict = {}
    countNum = 0

    for i in set(tangerine):
        dict[i] = 0

    for i in tangerine:
        dict[i] += 1

    sortList_tang = sorted((j for j in dict.values()), reverse = True)
    
    for i, j in enumerate(sortList_tang):
        countNum += j
        if (countNum >= k):
            return i + 1