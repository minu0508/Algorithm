from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    dq_people = deque(people)

    while len(dq_people) > 1:
        if (dq_people[0] + dq_people[-1] <= limit):
            dq_people.popleft()
        dq_people.pop()
        answer += 1
    if (dq_people):
        answer += 1
    
    return answer