import collections as col
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    rep = col.defaultdict(set)
    count = col.defaultdict(int)
    for i in report:
        Save1, Save2 = i.split(" ")
        rep[Save1].add(Save2)
        count[Save2] += 1
            
        
    for j in range(len(id_list)):
        for l in rep[id_list[j]]:
            if (count[l] >= k):
                answer[j] += 1

    return answer