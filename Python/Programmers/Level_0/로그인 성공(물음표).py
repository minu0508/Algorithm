def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                answer = "login"
                break
            else:
                answer = "wrong pw"
                break
    else:
        answer = "fail"
    return answer