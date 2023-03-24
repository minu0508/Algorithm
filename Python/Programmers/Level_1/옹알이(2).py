def solution(babbling):
    answer = 0
    Save_list = []
    Plus = 0

    for i in babbling:
        i = i.replace("aya", "*")
        i = i.replace("ye", "!")
        i = i.replace("ma", "$")
        i = i.replace("woo", "%")
        Save_list.append(i)

    for k in Save_list:
        if (len(k) == 1):
            if (k == "*" or k == "!" or k == "$" or k == "%"):
                answer += 1

        else:
            Plus = k.count("*") + k.count("!") + k.count("$") + k.count("%")
            if (Plus == len(k)):
                for l in range(0, len(k)-1, 1):
                    if (k[l] == k[l + 1]):
                        result = 0
                        break
                    else:
                        result = 1
                if (result == 1):
                    answer += 1
            else:
                pass
    return answer