def solution(s):
    answer = ''
    s = s.split(" ")
    print(s)
    for i in s:
        if (i == ''):
            answer += " "
        else:
            answer += i.capitalize()
            answer += " "

    return answer[:-1]

solution("3peo   ple unFollowed me")