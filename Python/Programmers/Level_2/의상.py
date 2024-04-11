def solution(clothes):
    array = {}
    
    for i in clothes:
        if i[1] in array:
            array[i[1]].append(i[0])
        else:
            array[i[1]] = [i[0]]

    clotheQuan = []
    for i in array.values():
        clotheQuan.append(len(i) + 1)
    
    clotheComb = 1
    for i in clotheQuan:
        clotheComb *= i

    return clotheComb - 1