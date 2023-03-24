def solution(numbers, direction):
    answer = []
    if (direction == "right"):
        Save = numbers.pop()
        numbers.insert(0, Save)
    elif (direction == "left"):
        Save = numbers[0]
        numbers.remove(numbers[0])
        numbers.append(Save)
    answer = numbers
        
    return answer