def solution(cipher, code):
    answer = ''
    cipher = list(str(cipher))
    Save = code
    for i in range(0, len(cipher)+1, 1):
        if (i % code == 0):
            answer += cipher[(code - 1)]
            code += Save
    return answer