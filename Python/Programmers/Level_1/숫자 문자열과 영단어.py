def solution(s):
    number_KR = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i in number_KR:
        if (s.count(i) >= 1):
            s = s.replace(i, number[number_KR.index(i)])
    
    return int(s)