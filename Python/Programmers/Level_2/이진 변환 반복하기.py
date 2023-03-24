def solution(s):
    answer = []
    step = 0
    zero_count = 0

    while(True):
        if (s == "1"):
            answer = [step, zero_count]
            break
        else: 
            zero_count += s.count("0")
            s = s.replace("0", "")
            s = str(bin(len(s))[2:])
            step += 1
        
    return answer