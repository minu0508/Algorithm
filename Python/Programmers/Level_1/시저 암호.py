def solution(s, n):
    s = list(s)
    answer = ''
    num = 0

    for i in s:
        if i == ' ':
            answer += i
        else:
            if (65 <= ord(i) <= 90):
                num = ord(i) + n
                if (num >= 91):
                    num -= 26
            elif (97 <= ord(i) <= 122):
                num = ord(i) + n
                if (num >= 123):
                    num -= 26
            answer += chr(num)
    return answer