from string import ascii_lowercase

def solution(s, skip, index):
    answer = ''
    alpha = list(ascii_lowercase)

    for i in skip:
        alpha.remove(i)
        
    for j in s:
        answer += alpha[(alpha.index(j) + index) % len(alpha)]

    return answer