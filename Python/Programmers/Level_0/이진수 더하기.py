def solution(bin1, bin2):
    Plus = list(map(int, str(int(bin1) + int(bin2))))
    answer = ''
    Save_Number = 0
    Num = 1

    for j in range(len(Plus)-1, -1, -1):
        Save_Number += (Plus[j] * Num)
        Num *= 2

    Bin = bin(Save_Number)

    for i in range(2, len(Bin), 1):
        answer += str(Bin[i])
    return answer