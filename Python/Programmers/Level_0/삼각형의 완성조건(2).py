def solution(sides):
    answer = 0
    answer_list = []
    tall = 0
    small = 0
    if (sides[0] > sides[1]):
        tall = sides[0]
        small = sides[1]
    else:
        tall = sides[1]
        small = sides[0]
        
    for i in range(1, tall+1, 1):
        if (tall < small+i):
            answer_list.append(i)
            if (tall == small+i):
                break
            
    
    answer = (len(answer_list) + (len(answer_list) - 1))
    return answer
