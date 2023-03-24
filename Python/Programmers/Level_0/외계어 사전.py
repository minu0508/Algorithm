def solution(spell, dic):
    answer = 0
    for i in range(len(dic)):
        Spell_Num = 0
        for j in spell:
            if (dic[i].count(j) >= 1):
                Spell_Num += 1
        if (len(spell) == Spell_Num):
            answer += 1
    if (answer >= 1):
        answer = 1
    else:
        answer = 2
    return answer
